# Sharing environment variables across Xcode Cloud workflows

**Framework**: Xcode

Apply common configurations to multiple workflows by using shared environment variables.

#### Overview

You can use shared environment variables in your custom build scripts to extend workflows. For example, use a shared environment variable for the location of an IPA file. Then you can edit the values of common environment variables in one location.

Before you begin, configure your project to use Xcode Cloud and create two or more workflows to share environment variables with.

##### Manage Shared Environment Variables in Xcode

To create shared environment variables in Xcode:

1. Open your project, click the Report navigator button in the navigator bar, and then click the Cloud button.
2. In the sidebar, Control-click your project name and choose Manage Environment Variables from the pop-up menu.
3. In the lower-left corner of the sheet, click the Add button (+).
4. In the Shared Environment Variables sheet, enter a name and value for the variable.
5. To securely store the variable and make sure it doesn’t appear in any logs, select the “Keep value redacted” checkbox in the Secret section.
6. To restrict editing of the alias to team roles, select the Only the Account Holder checkbox in the Restrict Editing section.
7. Click Next.
8. In the Select Workflows sheet, select the workflows you want to apply the environment variable to and then click Save.
9. In the Shared Environment Variables sheet, click Done.

To edit or delete environment variables in the Shared Environment Variables sheet before you click Done, Control-click the variable, and then choose Edit or Delete.

> 💡 **Tip**: You can also choose Integrate > [Your project name] > Manage Shared Environment Variables to create, edit, or delete environment variables.

To apply environment variables to workflows in Xcode:

1. In the Report navigator, Control-click your project name and choose Manage Workflows from the pop-up menu.
2. In the detail area of the sheet, Control-click the workflow you want to apply environment variables to, and then choose Edit from the pop-up menu.
3. In the sidebar, click Environment.
4. Under Environment Variables, select the environment variables to apply to the workflow.
5. Click Save.

To create another environment variable, click the Add button and choose New Shared Environment Variable from the pop-up menu.

##### Manage Shared Environment Variables in App Store Connect

You can also apply shared environment variables to workflows in App Store Connect with the following steps:

1. Sign in to your App Store Connect account and go to your app’s page.
2. Click the Xcode Cloud tab.
3. In the sidebar, click Settings.
4. Click the Shared Environment Variables tab.
5. Next to Shared Environment Variables, click the Add button.
6. In the New Shared Environment Variable sheet, enter a name and value for the variable.
7. To securely store the variable and make sure it doesn’t appear in any logs, select the Secret checkbox.
8. To restrict editing of the alias to team roles, select the Only the Account Holder checkbox.
9. Click Next.
10. In the Select Workflows sheet, select the workflows you want to apply the environment variable to.
11. Click Save.

To edit or delete custom aliases, click More (…) next to the environment variable and choose Edit or Delete from the pop-up menu.

## See Also

- [Making dependencies available to Xcode Cloud](making-dependencies-available-to-xcode-cloud.md)
  Review dependencies and make them available to Xcode Cloud before you configure your project to use Xcode Cloud.
- [Configuring Xcode Cloud for your team](configuring-xcode-cloud-for-your-team.md)
  Start using continuous integration and delivery with Xcode Cloud as a team.
- [Sharing macOS and Xcode versions across Xcode Cloud workflows](sharing-custom-aliases-across-xcode-cloud-workflows.md)
  Use custom aliases to share configurations with multiple workflows.
- [Building Swift packages and Swift Playgrounds app projects with Xcode Cloud](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md)
  Add your Swift package or Swift Playgrounds app project to an Xcode project to build it in Xcode Cloud.
- [Setting the next build number for Xcode Cloud builds](setting-the-next-build-number-for-xcode-cloud-builds.md)
  Start numbering builds from a custom build number for your existing Mac app to avoid version collisions.
- [Including notes for testers with a beta release of your app](including-notes-for-testers-with-a-beta-release-of-your-app.md)
  Add text files to your Xcode project to provide notes to beta testers about what to test.
- [Removing your project from Xcode Cloud](removing-your-project-from-xcode-cloud.md)
  Remove your project from Xcode Cloud to delete app and workflow data, disconnect your Git repository, and remove the Slack integration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/sharing-environment-variables-across-xcode-cloud-workflows)*