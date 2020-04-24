from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from messenger.models import Thread, UserThread, Message
from django.contrib.auth.decorators import login_required
from messenger.forms import MessageForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


@login_required
def view_messages(request):
    '''View all messages of logged in user.'''

    # query data (all threads + messages of that user)
    threads = {}
    all_threads = UserThread.objects.filter(user=request.user)
    print('all_threads', all_threads)
    for user_thread in all_threads:
        # retrieve messages from that thread
        messages = Message.objects.filter(thread=user_thread.thread)
        # figure out other user
        if user_thread.thread.user1 == request.user:
            other_user = user_thread.thread.user2
        else:
            other_user = user_thread.thread.user1
        # store messages from thread with other user
        threads[other_user] = messages

    return render(request, 'view_messages.html', {'threads': threads})


@login_required
def send_message(request):
    '''Logged in user sends message to specified recipient.'''

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.from_user = request.user
            receiving_user = User.objects.get(pk=request.GET['receiving_user_id'])
            message.to_user = receiving_user

            # inefficient way of checking whether thread exists
            # request.user.is_authenticated # wake up SimpleLazyObject
            print('from user', request.user, 'to_user', receiving_user)
            try:
                thread = Thread.objects.get(user1=request.user, user2=receiving_user)
            except ObjectDoesNotExist:
                try:
                    thread = Thread.objects.get(user1=receiving_user, user2=request.user)
                # if not, create thread and userthread
                except ObjectDoesNotExist:
                    thread = Thread(user1=request.user, user2=receiving_user)
                    thread.save()
                    # add user threads for both users
                    userthread = UserThread(user=request.user, thread=thread)
                    userthread.save()
                    userthread = UserThread(user=receiving_user, thread=thread)
                    userthread.save()
            message.thread = thread
            message.save()
            return redirect('view_messages')
        else:
            messages.error(request, 'Form not valid')

    else:

        receiving_user_id = request.GET['receiving_user_id']
        receiving_user = User.objects.get(pk=receiving_user_id)
        form = MessageForm()

        # show previous messages
        thread = None
        try:
            thread = Thread.objects.get(user1=request.user, user2=receiving_user)
        except ObjectDoesNotExist:
            try:
                thread = Thread.objects.get(user1=receiving_user, user2=request.user)
            # if not, create thread and userthread
            except ObjectDoesNotExist:
                history = None
        if thread:
            history = Message.objects.filter(thread=thread)


    data = {'form': form, 'receiving_user':receiving_user, 'history':history}

    return render(request, 'send_message.html', data)
