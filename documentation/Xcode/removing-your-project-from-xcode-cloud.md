# Removing your project from Xcode Cloud

**Framework**: Xcode

Remove your project from Xcode Cloud to delete app and workflow data, disconnect your Git repository, and remove the Slack integration.

#### Overview

When your app or framework is no longer under active development, you might want to do some general cleanup, like:

- Remove your app and any data from Xcode Cloud.
- Disconnect Xcode Cloud from your SCM provider.
- Disconnect Xcode Cloud from your team’s [`Slack`](https://developer.apple.comhttps://slack.com/) workspace.
- Remove any webhooks that you’ve configured.

##### Deleting Your Data From Xcode Cloud

When you delete your data from Xcode Cloud, you can’t restore it and it becomes immediately inaccessible.

Similarly, deleting a workflow deletes the workflow’s build history and artifacts. Only delete a workflow or your data from Xcode Cloud when you’re confident that you don’t need its build history or artifacts anymore. Instead, deactivate workflows you no longer need as described in [`Deactivate a workflow instead of deleting it`](developing-a-workflow-strategy-for-xcode-cloud#Deactivate-a-workflow-instead-of-deleting-it.md).

To stop using Xcode Cloud for your app or framework and delete its associated data:

- In Xcode, navigate to the Report navigator, Control-click your app, choose Delete Xcode Cloud Data for,” and confirm that you want to permanently delete all Xcode Cloud data.
- In [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com), go to your app’s page, select the Xcode Cloud tab, choose Settings > Delete Xcode Cloud Data, click Delete, and confirm that you want to permanently delete all Xcode Cloud data.

For more information on the differences between deleting and deactivating a workflow, see [`Deactivate a workflow instead of deleting it`](developing-a-workflow-strategy-for-xcode-cloud#Deactivate-a-workflow-instead-of-deleting-it.md).

##### Disconnect Your Git Repository in Xcode Cloud

If you move your Git repositories to another source code management (SCM) provider, you’ll want to remove the old provider from your Xcode Cloud configuration.

To disconnect Xcode Cloud from [`Bitbucket Server`](https://developer.apple.comhttps://bitbucket.org/product/enterprise), [`GitHub Enterprise`](https://developer.apple.comhttps://github.com/enterprise), or a [`self-managed GitLab instances`](https://developer.apple.comhttps://about.gitlab.com/install):

1. Sign in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) and go to Users and Access.
2. Select the Xcode Cloud tab.
3. Move the cursor over the SCM provider you want to remove, then click the Remove button (-) and confirm that you want to disconnect Xcode Cloud from your provider.

To disconnect Xcode Cloud from [`Bitbucket`](https://developer.apple.comhttps://bitbucket.org), [`GitHub`](https://developer.apple.comhttps://github.com), or [`GitLab`](https://developer.apple.comhttps://gitlab.com):

1. Sign in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) and go to your profile settings by clicking your account in the top-right corner of the website and Edit Profile.
2. Select the Xcode Cloud tab.
3. Choose Integrations in the sidebar.
4. Click Unlink next to the SCM provider you no longer use and confirm that you want to remove the connection between Xcode Cloud and your provider.

##### Remove Personal Access Tokens or Apps

To completely remove all traces of Xcode Cloud from your SCM provider, you need to remove the app or personal access token that allowed Xcode Cloud access to the repository. The process to do this is different for each SCM provider:

##### Remove the Slack Integration

If you connected your team’s Slack workspace to Xcode Cloud, the connection between Xcode Cloud and your Slack workspace remains when you delete a workflow or remove your project. To remove the Slack integration, you’ll need to uninstall the Slack app from your team’s Slack workspace:

1. Open your Slack workspace in your browser and click Manage. Alternatively, click on your workspace’s name in the Slack app and choose “Settings & administration” > “Manage apps”.
2. Choose Installed Apps in the sidebar, then choose the Xcode Cloud app.
3. Remove the app and confirm that you want to delete the Slack app for Xcode Cloud.

> **Note**: Depending on the configuration of your team’s Slack workspace, you may need to ask your team’s Slack administrator to remove the Slack app.

Depending on the configuration of your team’s Slack workspace, you may need to ask your team’s Slack administrator to remove the Slack app.

## See Also

- [Making dependencies available to Xcode Cloud](making-dependencies-available-to-xcode-cloud.md)
  Review dependencies and make them available to Xcode Cloud before you configure your project to use Xcode Cloud.
- [Configuring Xcode Cloud for your team](configuring-xcode-cloud-for-your-team.md)
  Start using continuous integration and delivery with Xcode Cloud as a team.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/removing-your-project-from-xcode-cloud)*