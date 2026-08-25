# Configuring Xcode Cloud for your team

**Framework**: Xcode

Start using continuous integration and delivery with Xcode Cloud as a team.

#### Overview

To adopt continuous integration and delivery (CI/CD) with Xcode Cloud, you’ll need to configure your project or workspace to use Xcode Cloud, create your first workflow, and then start your first build. However, starting to use Xcode Cloud as a team may require additional steps and coordination among team members and administrators — especially in a corporate context.

To successfully configure your team’s project or workspace to use Xcode Cloud, first review required roles and permissions described in [`Setting up your project to use Xcode Cloud`](setting-up-your-project-to-use-xcode-cloud.md). Depending on your role and permissions, you may need to coordinate with others to:

- Allow Xcode Cloud to access your team’s Git repository.
- Create an app record in App Store Connect.

If you have the required role and permissions to complete the above tasks or someone else has previously performed them, configure your team’s project or workspace to use Xcode Cloud as described in [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md). However, teams may limit the number of people who can administer their Git repositories and their App Store Connect account. In a corporate context, there might even be a dedicated infrastructure team, which means you need to work with them before you start using Xcode Cloud.

For additional information about using Xcode Cloud as a team, see [`Deep dive into Xcode Cloud for teams`](https://developer.apple.comhttps://developer.apple.com/wwdc22/110375).

##### Connect Xcode Cloud to an Admin Managed Git Repository

To start using Xcode Cloud, you need the permissions listed in [`Setting up your project to use Xcode Cloud`](setting-up-your-project-to-use-xcode-cloud.md) to grant Xcode Cloud access to your team’s Git repository. If you don’t have the required role or permission, work with your team’s source code management (SCM) administrator and ask them to configure your project to use Xcode Cloud.

You only need to work with your team’s SCM administrator when you onboard your team’s first app or framework to Xcode Cloud. When the SCM administrator configures Xcode Cloud for one project or workspace and connects your team’s SCM provider to Xcode Cloud, other projects you host with the same provider can use the configured connection. For example, say your team hosts its repositories on Bitbucket Cloud and your team’s administrator configures one project to use Xcode Cloud. When you start using Xcode Cloud for subsequent projects that use Bitbucket Cloud, you reuse the connection to Bitbucket Cloud that your administrator configured.

To connect Xcode Cloud to an admin-managed Git Repository:

1. Add your administrator to your team if they aren’t a member.
2. Let your administrator configure your project to use Xcode Cloud. If your repository’s administrator doesn’t have expertise developing for Apple platforms, it’s OK to let them configure your project or workspace to use Xcode Cloud and to allow the first build to fail.
3. Start using Xcode Cloud, as discussed in [`Connect your personal SCM account to Xcode Cloud`](configuring-xcode-cloud-for-your-team#Connect-your-personal-SCM-account-to-Xcode-Cloud.md) below, and fix any build issues as needed.

> 💡 **Tip**: If you host your code using [`GitHub`](https://developer.apple.comhttps://github.com) or [`GitHub Enterprise`](https://developer.apple.comhttps://github.com/enterprise), Xcode Cloud helps you work with your GitHub organization’s administrator. Start the initial configuration as described in [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md). When Xcode Cloud asks for permission to access your team’s repository, you can request that the *organization owner* or someone with the *admin* role installs the Xcode Cloud GitHub app that manages access to your team’s repositories. When the they’ve installed the app, you can complete the initial configuration.

##### Create an App Record in App Store Connect

Xcode Cloud combines [`Xcode`](https://developer.apple.comhttps://developer.apple.com/xcode/), [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/), and [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) into a powerful CI/CD system. As a result, you need an app record for your app in App Store Connect to use Xcode Cloud. If you haven’t created an app record for your app, Xcode helps you create one when you configure your project or workspace to use Xcode Cloud.

> **Note**: You don’t need to create an app record to build a framework with Xcode Cloud.

For more information about the requirements for creating an app record, see [`Set up your App Store Connect account`](setting-up-your-project-to-use-xcode-cloud#Set-up-your-App-Store-Connect-account.md). If you can’t create an app record, let someone who has the required role or permission create an app record in App Store Connect. Then configure your project or workspace to use Xcode Cloud as described in [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md).

##### Connect Your Personal Scm Account to Xcode Cloud

Xcode Cloud uses your personal SCM account to monitor the Git repository for changes. As a result, you need to connect your Xcode Cloud to your SCM account. To do this, open a project or workspace that another team member configured to use Xcode Cloud. If you haven’t connected your personal SCM account to Xcode Cloud, Xcode displays the Cloud Issues button in the toolbar. Click the button, and authorize Xcode Cloud to link your source control account with your Apple Account.

## See Also

- [Making dependencies available to Xcode Cloud](making-dependencies-available-to-xcode-cloud.md)
  Confirm that Xcode Cloud has access to every dependency your project needs to build.
- [Sharing macOS and Xcode versions across Xcode Cloud workflows](sharing-custom-aliases-across-xcode-cloud-workflows.md)
  Use custom aliases to share configurations with multiple workflows.
- [Sharing environment variables across Xcode Cloud workflows](sharing-environment-variables-across-xcode-cloud-workflows.md)
  Apply common configurations to multiple workflows by using shared environment variables.
- [Building Swift packages and Swift Playgrounds app projects with Xcode Cloud](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md)
  Add your Swift package or Swift Playgrounds app project to an Xcode project to build it in Xcode Cloud.
- [Setting the next build number for Xcode Cloud builds](setting-the-next-build-number-for-xcode-cloud-builds.md)
  Start numbering builds from a custom build number for your existing Mac app to avoid version collisions.
- [Including notes for testers with a beta release of your app](including-notes-for-testers-with-a-beta-release-of-your-app.md)
  Add text files to your Xcode project to provide notes to beta testers about what to test.
- [Removing your project from Xcode Cloud](removing-your-project-from-xcode-cloud.md)
  Remove your project from Xcode Cloud to delete app and workflow data, disconnect your Git repository, and remove the Slack integration.
- [Changing the bundle identifier](changing-the-bundle-identifier.md)
  Modify your app’s bundle identifier and update it anywhere it appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-xcode-cloud-for-your-team)*