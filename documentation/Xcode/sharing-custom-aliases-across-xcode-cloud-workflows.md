# Sharing macOS and Xcode versions across Xcode Cloud workflows

**Framework**: Xcode

Use custom aliases to share configurations with multiple workflows.

#### Overview

Custom aliases let you set up and manage common Xcode and macOS configurations that you can apply to multiple workflows. For example, create custom aliases to change Xcode versions for multiple workflows in one place. You can manage custom aliases in Xcode and in App Store Connect.

Before you begin, configure your project to use Xcode Cloud and create two or more workflows to share custom aliases with.

##### Manage Custom Aliases in Xcode

To create custom aliases in Xcode:

1. Open your project, click the Report navigator button in the navigator bar, and then click the Cloud button.
2. In the sidebar, Control-click your project name and choose Manage Custom Aliases from the pop-up menu.
3. In the lower-left corner of the sheet, click the Add button (+) and choose a configuration for the alias (either macOS or Xcode) from the pop-up menu that appears.
4. In the sheet that appears, enter a name for the alias, and choose the macOS or Xcode version from the Version menu to associate the alias with.
5. To restrict editing of the alias to team roles, select the Only the Account Holder checkbox in the Restrict Editing section.
6. Click Save and then click Done in the Custom Aliases sheet.

To quickly modify aliases in the Custom Aliases sheet before you dismiss it, Control-click the alias and choose Edit or Delete from the pop-up menu. To change permissions, choose either Restrict Editing or Remove Restrictions from the menu.

> 💡 **Tip**: You can also choose Integrate > [Your project name] > Manage Custom Aliases to create, edit, or delete custom aliases.

To apply custom aliases to workflows in Xcode:

1. In the Report navigator, Control-click your project name and choose Manage Workflows from the pop-up menu.
2. In the detail area of the sheet, Control-click the workflow you want to apply custom aliases to, and then choose Edit from the pop-up menu.
3. In the sidebar of the sheet that appears, click Environment.
4. From either the Xcode Version or the macOS Version pop-up menu, choose your custom alias.
5. Click Save.

To create another custom alias, choose New [Xcode | macOS] Version Alias or Manage Custom Aliases from the Version pop-up menu in the Environment sheet.

##### Manage Custom Aliases in App Store Connect

You can also apply custom aliases to workflows in App Store Connect with the following steps:

1. Sign in to your App Store Connect account and go to your app’s page.
2. Click the Xcode Cloud tab.
3. In the sidebar, click Settings.
4. Click the Custom Aliases tab.
5. Next to Custom Aliases, click the Add button and choose a configuration for the alias (either macOS or Xcode) from the pop-up menu that appears.
6. Enter a name for the alias, and choose the macOS or Xcode version to associate the alias with from the Version menu.
7. To restrict editing of the alias to team roles, select the Only the Account Holder checkbox.

To edit or delete custom aliases, click More (…) next to the alias and choose Edit or Delete from the pop-up menu.

To apply custom aliases to a workflow in App Store Connect:

1. On the Xcode Cloud page for your app, click Manage Workflows in the sidebar.
2. Select the workflow to apply the custom alias to.
3. From either the Xcode Version or the macOS Version pop-up menu, choose your custom alias.
4. Click Save.

## See Also

- [Making dependencies available to Xcode Cloud](making-dependencies-available-to-xcode-cloud.md)
  Review dependencies and make them available to Xcode Cloud before you configure your project to use Xcode Cloud.
- [Configuring Xcode Cloud for your team](configuring-xcode-cloud-for-your-team.md)
  Start using continuous integration and delivery with Xcode Cloud as a team.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/sharing-custom-aliases-across-xcode-cloud-workflows)*