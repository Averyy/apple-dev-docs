# Connecting Xcode Cloud to GitHub Enterprise

**Framework**: Xcode

Allow Xcode Cloud to access your GitHub Enterprise repository.

#### Overview

When you first configure your project or workspace to use Xcode Cloud, you need to allow Xcode Cloud to access your Git repository. It uses this access to automatically build and test your code when you make changes to the codebase.

If you host your code as part of a GitHub organization, the person who first configures a project to use Xcode Cloud must be an . If you don’t use a GitHub organization, the person who first configures a project to use Xcode Cloud must have the  permission. If you don’t have the required role or permission, see [`Connect Xcode Cloud to an admin-managed Git repository`](configuring-xcode-cloud-for-your-team#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository.md).

If your GitHub Enterprise instance settings have an IP allow list, make sure that you have added [`our IP address ranges`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/Setting-up-your-project-to-use-Xcode-Cloud#Use-a-remote-source-control-repository) to it before proceeding.

To allow Xcode Cloud to access your repository on [`GitHub Enterprise`](https://developer.apple.comhttps://github.com/enterprise):

1. Configure your project or workspace to use Xcode Cloud and create your first workflow as described in [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md). Xcode analyzes your project to learn which SCM provider you use and then displays the URL of your GitHub Enterprise instance on the Grant Access to Your Source Code sheet.
2. Click Grant Access. Xcode opens your browser and takes you to the [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) website.
3. Choose GitHub Enterprise.
4. Register the host name of your GitHub Enterprise host. The corresponding field should already contain your instance’s URL. Check if it’s correct; for example, make sure it contains a required port.
5. Click Complete Step 1 in GitHub Enterprise to navigate to the website of your GitHub Enterprise host.
6. Review the name of the GitHub app, then create it. GitHub Enterprise uses this app to grant Xcode Cloud access to your repository.
7. Review and authorize the permissions that the GitHub app requests.
8. Authorize Xcode Cloud to verify your identity on GitHub Enterprise to link your GitHub Enterprise account to your Apple Account.
9. Choose to only install the GitHub app for your project’s repository. Don’t install it for every repository. When the installation finishes, GitHub Enterprise takes you back to the App Store Connect website. App Store Connect now indicates that you successfully connected Xcode Cloud to GitHub Enterprise.
10. Return to Xcode. It indicates that Xcode Cloud can access your source code.
11. Click Next, complete your first workflow, and start your first build.

## See Also

- [Connecting Xcode Cloud to GitHub](connecting-xcode-cloud-to-github.md)
  Allow Xcode Cloud to access your GitHub repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-github-enterprise)*