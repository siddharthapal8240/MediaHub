from django.shortcuts import render
from .models import Tweet, Like, Comment
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    query = request.GET.get('q')
    comment_filter = request.GET.get('comment_filter', 'all')  

    if query:
        tweets = Tweet.objects.filter(text__icontains=query).order_by('-created_at')
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
    
    # Get the IDs of tweets liked by the current user
    liked_tweets = Like.objects.filter(user=request.user) if request.user.is_authenticated else []
    liked_tweet_ids = liked_tweets.values_list('tweet', flat=True) if liked_tweets else []

    # Loop through each tweet to filter comments
    for tweet in tweets:
        if comment_filter == 'newest':
            tweet.comments = tweet.comment_set.all().order_by('-created_at')  
        else:
            tweet.comments = tweet.comment_set.all().order_by('created_at')  

    return render(request, 'tweet_list.html', {
        'tweets': tweets,
        'liked_tweet_ids': liked_tweet_ids,  
        'comment_filter': comment_filter  
    })

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

# New view to like a tweet
@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    like, created = Like.objects.get_or_create(tweet=tweet, user=request.user)

    if not created:  
        like.delete()
        tweet.likes_count -= 1  
    else:
        tweet.likes_count += 1  
    
    tweet.save() 

    return redirect('tweet_list')

# Comment on a tweet
@login_required
def comment_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(tweet=tweet, user=request.user, content=content)

    return redirect('tweet_list')
