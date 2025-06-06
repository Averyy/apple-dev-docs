# Connecting Xcode Cloud to Bitbucket Server

**Framework**: Xcode

Allow Xcode Cloud to access your Bitbucket Server repository.

#### Overview

When you first configure your project or workspace to use Xcode Cloud, you need to allow Xcode Cloud to access your Git repository. It uses this access to automatically build and test your code when you make changes to the codebase.

The person who first configures a project or workspace to Xcode Cloud must have the  permission for its repository on Bitbucket Server. If you don’t have this permission, see [`Connect Xcode Cloud to an admin-managed Git repository`](configuring-xcode-cloud-for-your-team#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository.md).

To allow Xcode Cloud to access your repository on [`Bitbucket Server`](https://developer.apple.comhttps://bitbucket.org/product/enterprise):

1. Configure your project or workspace to use Xcode Cloud and create your first workflow as described in [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md). Xcode analyzes your project to learn which SCM provider you use and then displays the URL of your Bitbucket Server host on the Grant Access to Your Source Code sheet.
2. Click Grant Access. Xcode opens your browser and takes you to the [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) website.
3. Enter the host name of your Bitbucket Server instance on the App Store Connect website. When it analyzes your project, Xcode Cloud learns the host name of your Bitbucket Server instance and fills the corresponding field on the website for you.
4. Check if the entered host name is correct (for example, make sure it contains a required port) and click Register.
5. Click “your Bitbucket Server host”. This opens your Bitbucket Server instance and displays your account’s “Personal access tokens” section. Don’t close the tab or window that displays the Xcode Cloud webpage.
6. Click “Create a token” to start the creation of a personal access token that Xcode Cloud uses to access your repositories.
7. Enter a name for the access token that’s easy to recognize; for example, `Xcode Cloud`.
8. Configure the token to have the  permission for projects and the  permission for repositories.
9. Create the token and make sure to copy and store it in a safe place before continuing. Bitbucket Server won’t show this information again. For example, you can create a secure note in Keychain Access and add the token to it.
10. Switch back to the browser tab or window that displays the App Store Connect website where you started connecting Xcode Cloud to Bitbucket Server.
11. Paste your personal access token into the corresponding field.
12. Click Register. App Store Connect indicates that you successfully connected Xcode Cloud to Bitbucket Server.
13. Return to Xcode. It indicates that Xcode Cloud can access your source code.
14. Click Next, complete the configuration of your first workflow, and start your first build.

## See Also

- [Connecting Xcode Cloud to Bitbucket Cloud](connecting-xcode-cloud-to-bitbucket-cloud.md)
  Allow Xcode Cloud to access your Bitbucket Cloud repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-bitbucket-server)*