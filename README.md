# What This Project is About
This is a project that I made solo during the MacHacks hackathon from Feb 3-5, 2023. My primary goal for this hackathon was to experiment with web development and the way in which people interacts with natural language models through simple user interfaces. I feel that it is important to mention that this is, indeed, my first project in the web development domain. I am not a web designer nor do I know a lot about web technologies. This project essentially served as a deep dive into the world of web so that I can determine if this is a specialization that I might enjoy. Given more time to develop this project, along with more knowledge of various web frameworks and technologies, the result could've been more promising.
# How to use the project
There are two primary dependencies that Tidy utilizes: Django and Openai. You can install them by simply running

pip3 install django

pip3 install openai

To keep Tidy as a secure application, both the Django signing key and the OpenAI api key are stored as environment variables. Once you have generated an appropriate Django key and have an API key, store them as djangokey and openaikey respectively. Then run

python manage.py runserver

This will open a local instance of the program on your machine and a link will be provided to view it.
# Inspiration
Motivating people to act more environmentally friendly is a difficult problem that could potentially result in the reduction of climate change and pollution. One simple way to achieve this is by reusing items rather than constantly producing new ones. Selling or recycling used items can be a chore for many people, which often results in them simply throwing out the item, which is disadvantageous ecologically. Automating this process, or making it easier, could help to motivate people to think more environmentally and take steps towards reducing pollution and unnecessary production.
# What it does
Based on the particular item that you want to sell, Tidy asks you to provide specific information regarding your product along with an image. Based on this information, Tidy uses OpenAI's GPT-3 natural language processor to generate a title for the listing as well as a convincing description for your item, to make the selling process easier. Rather than forcing you to spend lots of time making the perfect photos of your item, Tidy uses OpenAI's DALL-E variation algorithm to create better images of your item to post on a platform of your choice, namely, Kijiji. 
# How I built it
I built the application starting with the front end. This is, by far, my weakest area in web development and thus took the longest (with very mediocre results). The front end was built primarily with HTML and CSS, with a tiny bit of JavaScript to make the form more interactive. Having completed most of the front end, I linked it to a Django backend. I then added a module that interfaces with OpenAI's GPT-3 and DALL-E APIs to generate titles, descriptions, and image variations. The backend would then place these suggestions onto another webpage, which is viewable by the user. If time permitted, I would have used selenium to take these images and descriptions and made it automatically create a Kijiji listing. 
# Accomplishments that I'm proud of
This is my first web development project ever. It has truly been an amazing and educational experience. I learned a lot about how the front end interacts with the backend, file uploads, form validation, API requests, etc. 
# What's next for Tidy
Tidy is ultimately a proof-of-concept that is meant to show that complex tasks can be automated using natural language models. As a result of this automation, it alleviates the barrier to entry for acting in an ecologically-friendly manner. It essentially reduces the amount of effort required by the user which, hopefully, results in the user acting in an environmentally-beneficial way. It also serves as a proof-of-concept on how natural language models can be used to automate the sales process. GPT-3 can essentially serve as an expert salesman. To further develop this application, adding more product categories, customizability, and the ability to post directly onto Kijiji are the immediate first steps. Furthermore, refining DALL-E's image variations can prove to be extremely beneficial when creating convincing listings, as the images generated are often cartoonish and are not representative of the actual product. 
