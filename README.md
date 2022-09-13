# Simple CRUD Service Template - Node.js

This is a template for a simple CRUD service with an API, a function and a table.
After you create a project from this template, change and extend it to fit your
specific requirements.

## Before you begin

### 1. Create a free Altostra account
To create an account, simply login to the [Altostra Web Console](https://app.altostra.com).

### 2. Install the Altostra CLI
```sh
# make sure you have Node.js 10 or above installed
$ npm install -g @altostra/cli
```

### 3. Connect an a AWS account
To connect an AWS account, click **Connect Cloud Account** on the [Web Console settings](https://app.altostra.com/settings) page.

> If you don't wish to connect your account just yet, you can deploy to the [Playground](https://docs.altostra.com/reference/concepts/playground-environment.html) environment that simulates the cloud without creating actual resources.

## Using the template

You have several options to get started with this template:
* Initialize a new project from the Altostra CLI and specify the template:

```sh
$ mkdir simple-crud-service
$ cd simple-crud-service
$ alto init --template simple-crud-service-python
```

* Create a new project from the [Altostra Web Console](https://app.altostra.com/projects), you can select the `simple-crud-service-python` template from the list.

* Apply the template to an existing Altostra project from Visual Studio Code by going to the Altostra view in the main toolbar and clicking on `simple-crud-service-python` in the templates list.

## Deploying the project

Start by logging in from the Altostra CLI:
```sh
$ alto login
```

>The deployment process is simple and involves a few commands.
>For more information on each command refer to the [Altostra CLI documentation](https://docs.altostra.com/reference/CLI/altostra-cli.html).

Create an [image](https://docs.altostra.com/howto/projects/deploy-project.html#create-a-project-image) of the project:
```sh
$ alto push v1.0
```

Deploy the image as a new
[deployment](https://docs.altostra.com/reference/concepts/deployments.html) named `main` in the `Production` environment:
```sh
# omit "--new Production" to update rather than create
$ alto deploy main:v1.0 --new Production
```

## View the deployment status and details
You have two options, list the deployment details in the terminal or open the Web Console.

* Using the Altostra CLI:
```sh
# list the deployments for the current project
$ alto deployments

# show details for the deployment "main"
$ alto deployments main
```

* Using the Web Console:
```sh
# will open the Web Console for the current project
$ alto console
```

## Modifying the project
To modify the project, install Altostra Tools for Visual Studio Code:

From the terminal:
```sh
$ code --install-extension Altostra.altostra
```

or, search for Altostra Tools in the Visual Studio Code extensions view.

or, directly from the [marketplace](https://marketplace.visualstudio.com/items?itemName=Altostra.altostra).

> The extension adds an Altostra panel and visual additor that help you modify and
> design the project infrastructure.

## Template content

### Cloud resources
* REST-API
* Functions (Node.js runtime)
* Data Table

### Source files
The source files are located in the `functions` directory.
