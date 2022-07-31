This code was created by Logan Maupin aka Voltaic314 on GitHub. I am a student at the University of Arizona studying Applied Computing - Applied Artificial Intelligence. My hopes is that one day with my degree I will be able to contribute to Natural Language Processing Machine Learning models. -- However, this code was not a direct result of my education and came primarily *BEFORE* all of my coding classes. I created this code as a general way to practice coding and also because I wanted to work on a project that I personally enjoyed. I had this idea for this page and code idea from the page on FB called "Daily Updates on the Status of Michael Jackson's Health Condition", which is a much larger page than mine. It post irregularly and I wanted to make a page that would post consistently. 

#########################################################

PLEASE NOTE: If you try to run this code yourself without doing any prep work, you will run into errors. I'm not gonna write an entire guide here on how to get this code to work. But I will do you the favor of listing out all the basic steps to make this work. 

1. you will need to make a fb page (or use an existing one) -- duh...

2. you will need to create a developers account on fb to grant you api access. Trust me, you don't want to web scrape this. I've lost many hours trying to web scrape obvious things that can be API'd. Don't do it. Use it as a last resort (and even then most websites will detect your bots, good luck). 

3. once you create a fb page and developer account, you will need to create a blank "app" on the fb developer page dashboard. Basically this app is just so that you can have api access and fb can generate api tokens specific to your "app" so they know which token is doing all the API calls. This code only calls an API however many times you are posting to FB. I don't think this is very scaleable, I think FB hard caps your API calls to a relatively low number for large scale operations. but for small projects like this it's perfectly fine. 

4. once you set up the "app" on the developer page, you just need to generate an API token that has permissions to post. This part is tricky because FB has like 3 different API tokens, a short term one that expires in about an hour, a semi-short term one that expires after a few days or weeks if I remember correctly, and then a long term perma-one. the permanent one is the one you want to get. FB has an article showing how to retrieve this one. Just make sure that your temporary ones first have all the permissions you want / need before you start using your perma one. Here's the article link: https://developers.facebook.com/docs/pages/publishing/ 

5. Once you have that, you can create a variable in Python that holds your permanent access token to be referenced in the later lines as you can see in my code. But ideally you would create a config.py file, separate from your main code, that holds the variable safe for you in case you ever need to post the code or need it inspected or something. 

anyways once you do all those things you should be good to go. 

But one final note: My code runs off an AWS free server and uses crontab to schedule posts everyday. Meaning that it schedules when to run the script which is why there is no schedule feature. If you truly want to automate this, you'll need to use something like windows task scheduler, crontab, or other equivalent to automate it's posting every day. Alternatively Python has a schedule function you can use if you import the schedules package, but that means your code has to run basically 24/7 which is inefficient and kind of silly to do for something like this, but maybe not a bad idea depending on your use of this code. 

As always, any suggestions to make the code better or more efficient is always welcome. Thanks for reading and i hope you guys enjoy it. 
