# Connecting Xcode Cloud to GitHub

**Framework**: Xcode

Allow Xcode Cloud to access your GitHub repository.

#### Overview

When you first configure your project or workspace to use Xcode Cloud, you need to allow Xcode Cloud to access your Git repository. It uses this access to automatically build and test your code when you make changes to the codebase.

If you host your code as part of a GitHub organization, the person who first configures a project to use Xcode Cloud must be an . If you don’t use a GitHub organization, the person who first configures a project to use Xcode Cloud must have the  permission. If you don’t have the required role or permission, see [`Connect Xcode Cloud to an admin-managed Git repository`](configuring-xcode-cloud-for-your-team#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository.md).

To allow Xcode Cloud to access your repository on [`GitHub`](https://developer.apple.comhttps://github.com):

1. Configure your project or workspace to use Xcode Cloud and create your first workflow as described in [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md). Xcode analyzes your project to learn which SCM provider you use and then indicates that you use GitHub.
2. Click Grant Access. Xcode opens your browser and takes you to the [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) website.
3. Click Complete Step 1 in GitHub to link your Apple Account with your GitHub account to open the GitHub website.
4. Review the permissions Xcode Cloud requests, and authorize Xcode Cloud to link your GitHub account to your Apple Account.
5. Review the GitHub app that Apple provides on the GitHub website and choose to only install it for your project’s repository. Don’t install it for every repository. GitHub uses the app to grant Xcode Cloud access to your repository.
6. Click Install to return to App Store Connect website. It indicates that you successfully connected Xcode Cloud to GitHub.
7. Return to Xcode. It indicates that Xcode Cloud can access your source code.
8. Click Next, complete the configuration of your first workflow, and start your first build.

## See Also

- [Connecting Xcode Cloud to GitHub Enterprise](connecting-xcode-cloud-to-github-enterprise.md)
  Allow Xcode Cloud to access your GitHub Enterprise repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-github)*