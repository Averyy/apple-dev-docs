# Connecting Xcode Cloud to GitLab

**Framework**: Xcode

Allow Xcode Cloud to access your GitLab repository.

#### Overview

When you first configure your project or workspace to use Xcode Cloud, you need to allow Xcode Cloud to access your Git repository. It uses this access to automatically build and test your code when you make changes to the codebase.

The person who first configures a project or workspace to use Xcode Cloud must have the  role for the GitLab repository. If you don’t have this role, see [`Connect Xcode Cloud to an admin-managed Git repository`](configuring-xcode-cloud-for-your-team#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository.md).

To allow Xcode Cloud to access your repository on [`GitLab`](https://developer.apple.comhttps://gitlab.com):

1. Configure your project or workspace to use Xcode Cloud and create your first workflow as described in [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md). Xcode analyzes your project to learn which SCM provider you use and indicates that you use GitLab on the Grant Access to Your Source Code sheet.
2. Click Grant Access. Xcode opens your browser and takes you to the [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) website.
3. Click “Authorize in GitLab” to open the GitLab website and install a GitLab app that manages access to your GitLab repository.
4. Review the permissions that Xcode Cloud requests and allow it to access your account. This takes you back to the App Store Connect website, which indicates that you successfully connected Xcode Cloud to GitLab.
5. Return to Xcode. It indicates that Xcode Cloud can access your source code.
6. Click Next, complete the configuration of your first workflow, and start your first build.

## See Also

- [Connecting Xcode Cloud to a self-managed GitLab instance](connecting-xcode-cloud-to-a-self-managed-gitlab-instance.md)
  Allow Xcode Cloud to access your self-managed GitLab repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-gitlab)*