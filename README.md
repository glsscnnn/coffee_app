## Coffee App ☕

The goal: coffee broker?


A better ethos: We want to take this complex supply chain of growing, processing and exporting beans and streamline this process so that roasters can easily just buy the beans that they want quickly easily without difficulty and get it to you. This application is just a proof of concept, for what an application this type of company would perhaps use to interact with their customers.


Why would I make this if I'm not going to use it or finish it? Yeah so I'm probably not going to finnish this app but I do want to learn Django I think the ability to use an MVC is incredibly broken and just for side projects in general MVCs are broken because I don't actually have to think, my main thing atm is AI so writing web applications and stuff is not something I want to think about too much although I could use React, React has it's problems that mostly come with it being unopinionated yes I could use Angular but Angular is trash. Django is also written in python making it very easy to integrate with ML/AI projects.


### A Note on Security and Reproducibility

Yes I know the secret key is public. In production and if you wanted to use this app please store this information in an enviornment variable or something this is not good what is in the repo. Also reproducibility, just copy the apps lol Django allows for pluggable app design so just make a new django project and plug the apps and makemigrations and what not.


### To View the App

Clone or download the repo, then run `python manage.py runserver` you may want to `python manage.py migrate` etc. before but that's up to you lol.