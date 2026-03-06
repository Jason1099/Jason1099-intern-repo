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
> clawhub install <skill name>

A list of skills can be seen in the [ClawHub](https://clawhub.ai/skills?sort=downloads) site. 

# QA Automation 
QA automation solutions can be done depending on the type of App (web, desktop, etc.). Setting up automatic testing for web apps is relatively easier to setup. 

In terms of desktop testing:
Based on initial research on solutions we could do:
1. Pywinauto script generation and execution with OpenClaw
   Pywinauto is a python module used to automate Microsoft Windows GUI. This depends on what framework the app is based of. In terms of


# Automated Task
Another possible idea would be to let Open Claw view the app visually (take snapshots) and do things like assisting in completing a todo list. This may also require
