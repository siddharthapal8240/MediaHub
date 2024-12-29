
# Project Name: MediaHub

Welcome to **MediaHub**, a dynamic and interactive social media platform built with Django. MediaHub allows users to post, comment, like, and manage their tweets seamlessly.

---

## Screenshots

Here are representations of MediaHub across various devices:

![MediaHub Screen Representations](/final_responsive_project.png)

---


## 🚀 Features
1. **User Authentication**: 
   - Register, login, and logout functionalities.
2. **Tweet Management**: 
   - Users can create, edit, and delete their tweets.
   - Character limit of 200 characters for tweet text.
3. **Like Functionality**: 
   - Users can like tweets, and the like count is displayed dynamically.
4. **Comments Section**: 
   - Users can add comments to tweets.
   - A single comment is displayed by default, with an option to view or filter all comments.
   - If no comments exist, a styled "No comments yet" message is displayed.
5. **Search Bar**: 
   - Allows users to search for tweets.
6. **Responsive Design**:
   - Mobile-friendly and optimized for various screen sizes.

---

## 🛠️ Technologies Used
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django
- **Database**: Postgresql
- **Media Handling**: Cloudinary
- **Icons**: FontAwesome

---

## 📂 Project Structure
```
MediaHub/
├── MediaHub/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── templates/
│       ├── layout.html
│       ├── registration/
│           ├── logged_out.html
│           ├── login.html
│           ├── register.html
├── tweet/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── templates/
│       ├── index.html
│       ├── tweet_confirm_delete.html
│       ├── tweet_form.html
│       ├── tweet_list.html
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
├── .gitignore
├── db.sqlite3
├── final_responsive_project.png
├── manage.py
├── README.md
├── requirements.txt

```

---

## Setup Instructions

Follow these steps to set up MediaHub locally:

### Prerequisites

1. Install Python (3.8 or above).
2. Install pip and virtualenv.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/siddharthapal8240/MediaHub.git
   cd MediaHub
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and configure the following environment variables:

   ```env
   ALLOWED_HOSTS=
   API_KEY=
   API_SECRET=
   CLOUD_NAME=
   CLOUDINARY_URL=
   DATABASE_URL=
   DEBUG=
   SECRET_KEY=
   ```

5. Run database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access MediaHub at `http://127.0.0.1:8000`.

---

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

---

## Contact

For any queries or suggestions, feel free to contact:

- **GitHub:** [siddharthapal8240](https://github.com/siddharthapal8240)
- **Email:** siddhartha.pal.official@gmail.com

---

Developed with ❤️ by Siddhartha Pal
