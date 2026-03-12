Open Claw is a dekstop AI agent / assistant that can have amazing uses and abilities. Notably multiple channels for communication (Whatsapp, Discord, Telegram, etc), and the ability to run and execute tasks directly on the desktop. It can also perform web searches, and web tasks through APIs, such as accessing the user's google services (gmail inbox, calendar, etc.) This [Link](https://o-mega.ai/articles/openclaw-creating-the-ai-agent-workforce-ultimate-guide-2026) has a good overview of it. 

# Installation
Open Claw has different installations for Linux based systems, and windows systems. For windows, the following steps are used:
1. Installing OpenClaw:
   iwr -useb https://openclaw.ai/install.ps1 | iex
2. Onboarding Wizard to get it setup with some configs:
   openclaw onboard --install-daemon

for more information, visit [OpenClaw](https://docs.openclaw.ai/start/getting-started#windows-powershell)

# Model Choices
Open Claw has a lot of options in what model or provider to use.
1. Cloud Models
   Open Claw can use most providers, such as OpenAI and Google, with ChatGPT and Gemini respectively. An API key needs to be provided. <br/>
   It is important to note that OpenClaw will use tokens quickly, which is a big bottleneck for free tier keys.

2. Local Models
   Open Claw can also be setup to run with a local model. For example, we may use Ollama to download a local model and launch Open Claw with that. <br/>
   An advantage of this setup is that it can be run fully offline, which is great for privacy and security issues. However, running a model powerful enough to utilise tools and perform tasks is difficult to do in a local machine due to its hardware requriements. Hence, this solutio may not be feasible for everyone


# Downlaoding Skills for OpenClaw
Open Claw can download skills to use through clawhub, by running:
> clawhub install "skill name"

A list of skills can be seen in the [ClawHub](https://clawhub.ai/skills?sort=downloads) site. 

# QA Automation 
QA automation solutions can be done depending on the type of App (web, desktop, etc.). Setting up automatic testing for web apps is relatively easier to setup. 

In terms of desktop testing:
Based on initial research on solutions we could do:
1. Pywinauto script generation and execution with OpenClaw
   Pywinauto is a python module used to automate Microsoft Windows GUI. This depends on what framework the app is based of.


# Automated Task
Another possible idea would be to let Open Claw view the app visually (take snapshots) and do things like assisting in completing a todo list. This would require Open Claw to have the neccesary skills to perform these tasks (such as the gog skill to access google servides)

# My Tests / Implementations so far

## QA Automation

As I've suggested before, a way we could do this is to utilise the pywinauto library to perform tasks directly in the desktop. <br/>
To see if it can detect and "see" the focus bear app, I used a test script to print out the list of control identifiers of the app. A printed out example can be seen in this [file](OpenClaw_Scripts/control_identifiers.txt) <br/>

Afterwards, I generated a script to run and interact with a button. In this case, I tested it to click the "habits" button. Some findings I've found:
1. It couldn't directly find a tree item called "Habits". It was a static item under a navleaf item, so it needed to find this text and click on the parent item. Open Claw wans't able to generate this code correctly even when given the list of identifiers
2. The list of Identifiers will always change depending on what's rendered on the screen
3. It needs to make sure that it targets the main screen (or the tray bar if that's whats intended), as it would return an error as there is more than 1 focus bear window. 
4. Open claw alse needs some configurations to allow it to run python scripts. In some occasions, it told me that it didn't have the capability to do so, even when I confirmed that it did.
5. Python libraries need to be installed prior for scripts to work. Didn't test whether open claw could or would download python libraries automatically. 

the python files can be found under the [OpenClaw Scripts Folder](OpenClaw_Scripts/)

Hence based on this:
1. Open Claw code generation (at least with the model I've tested, which is gpt-4o) is not good enough to handle these nuances and manage problems itself.
2. A workflow could be to let it run a python script that lists the current control identifiers available, and then generate a script that automatically handles a given set of instructions to do. It may be best to let it navigate to a "home" screen, like the to do list screen, and go from there. We also need it to handle waiting for items or pages to load before proceeding. 

## To Do List automation:
I haven't done much testing in this regard. Similar to QA automation, I made open claw run a script that takes a screenshot of the screen, allowing to read from it. My general idea for this was for reading to do lists items and letting open claw help with those. 

An implementation that I haven't tested would be to also use pywinauto to navigate to a specific item, such as the to do list, and scrape the items by printing out the list of identifiers. 

An important thing to note is that the above implementations would need to have the window open visually. Pywinauto also directly interacts with the app by moving the cursor and performing clicks, so it may be a hinder to the user. 
