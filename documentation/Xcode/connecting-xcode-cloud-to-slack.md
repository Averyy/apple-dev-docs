# Connecting Xcode Cloud to Slack

**Framework**: Xcode

Connect Xcode Cloud to Slack to keep your team informed about the latest Xcode Cloud builds.

#### Overview

Many teams use [`Slack`](https://developer.apple.comhttps://slack.com) to collaborate and expect other tools to support and integrate with Slack. And because collaboration is an important part of using Xcode Cloud, you can easily connect it to Slack and receive its notifications in your team’s Slack workspace.

By connecting Xcode Cloud to Slack, you can:

- Receive Xcode Cloud notifications in Slack that contain a build’s status and links to the build report.
- Configure Xcode Cloud to send notifications to you as direct messages, or choose a Slack channel for team-level notifications.
- Use different Slack channels for different workflows.

Use Xcode or [`App Store Connect`](https://developer.apple.comhtts://appstoreconnect.apple.com) to connect Xcode Cloud to a single Slack workspace.

> **Note**: Depending on your team’s Slack workspace settings, you may need to ask your team’s Slack administrator to connect Xcode Cloud to Slack. For more information, see [`Install the Slack app for Xcode Cloud using App Store Connect`](connecting-xcode-cloud-to-slack#Install-the-Slack-app-for-Xcode-Cloud-using-App-Store-Connect.md).

Depending on your team’s Slack workspace settings, you may need to ask your team’s Slack administrator to connect Xcode Cloud to Slack. For more information, see [`Install the Slack app for Xcode Cloud using App Store Connect`](connecting-xcode-cloud-to-slack#Install-the-Slack-app-for-Xcode-Cloud-using-App-Store-Connect.md).

##### Install the Slack App for Xcode Cloud Using Xcode

To connect Xcode Cloud to Slack, you’ll need to install the Slack app Apple provides into your Slack workspace. The app manages access to your team’s Slack workspace.

To install the Slack app using Xcode:

1. Choose Integrate > Manage Workflows to open the Manage Workflows sheet.
2. Double-click a workflow to open.
3. Click the Add button (+) next to Post-Actions and choose Notify to add a post-action for sending notifications. ![A screenshot of workflow in Xcode where the Notify - Successes and Failures post-action is visible.](https://docs-assets.developer.apple.com/published/8613e5cc41a84566c0f05c7590bc6ff0/Connecting-Xcode-Cloud-to-Slack-1%402x.png)
4. Click the Add button in the Slack section of the post-action you added.
5. Provide the name of your Slack workspace, then click Connect. This opens your team’s Slack workspace in your browser.
6. Sign in to your Slack workspace if you aren’t signed in already, and then review the permissions that the Slack app for Xcode Cloud requests.
7. Click Allow to install the app into your Slack workspace. This takes you to Xcode where you can now configure the Notify post-action to send build notifications to your team’s Slack channels as described in [`Choose a Slack channel`](connecting-xcode-cloud-to-slack#Choose-a-Slack-channel.md).

> 💡 **Tip**: Configure Xcode Cloud to send build notifications to yourself as direct messages (DMs) in Slack. Navigate to your account in App Store Connect, select the Xcode Cloud tab, choose Notifications in the sidebar, and select the checkbox next to Slack.

Configure Xcode Cloud to send build notifications to yourself as direct messages (DMs) in Slack. Navigate to your account in App Store Connect, select the Xcode Cloud tab, choose Notifications in the sidebar, and select the checkbox next to Slack.

##### Install the Slack App for Xcode Cloud Using App Store Connect

Another way to configure Xcode Cloud to send notifications to Slack is by setting up that connection in [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). It’s especially convenient if you need to work with your team’s Slack administrator to connect Xcode Cloud to Slack, because they don’t need to be familiar with Xcode.

If you work with your team’s Slack administrator, add them to your Apple Development team, and assign them one of the following roles: App Manager, Admin, or Account Holder. With the proper role set in App Store Connect, they can connect Xcode Cloud to Slack.

To connect Xcode Cloud to your team’s Slack workspace in App Store Connect:

1. Navigate to your app’s page in App Store Connect and select the Xcode Cloud tab.
2. Choose Manage Workflows in the sidebar and open a workflow by clicking its name.
3. Click the Add button next to Post-Actions and choose Notify to add a post-action for sending notifications.
4. Click Edit in the Slack section of the post-action you added.
5. Enter the name of your team’s Slack workspace, then click Connect. This opens your team’s Slack workspace.
6. Sign in to your Slack workspace if you aren’t signed in already, and then review the permissions that the Slack for Xcode Cloud requests.
7. Click Allow to install the app into your Slack workspace. This takes you back to your workflow in App Store Connect where you can now configure the Notify post-action to send build notifications to your team’s Slack channels.

You can also connect Xcode Cloud to Slack by clicking on your account in the top-right corner of the App Store Connect website and choosing Edit Profile. In your profile settings, select the Xcode Cloud tab, then click Connect next to Slack and install the Xcode Cloud app into your Slack workspace.

##### Grant Xcode Cloud Access to Your Slack Account

If you personally connected Xcode Cloud to Slack, you can configure Xcode Cloud to send build status notifications to your team’s Slack channels. You can also choose to receive build status notifications as direct messages. However, someone else may have connected Xcode Cloud to Slack; for example, the administrator of your team’s Slack workspace. In this case, you’ll receive build status notifications in Slack channels that your team member configured, but you need to authorize Xcode Cloud to use your Slack account before you can make changes to a workflow’s Notify post-action.

To authorize Xcode Cloud to access your Slack account:

1. Open a workflow in Xcode or App Store Connect.
2. Navigate to the Notify post-action.
3. Follow the guidance by Xcode or App Store Connect to grand Xcode Cloud access to your Slack account.

After authorizing Xcode Cloud to access your Slack account, you can make changes to your workflow’s Notify post-action and configure personal build notifications for Slack.

##### Choose a Slack Channel

Depending on your project, you can direct all Xcode Cloud notifications to the same Slack channel or to set up different Slack channels to receive the notifications. For example, use a single Slack channel for all Xcode Cloud notifications if you’re a solo developer or your team only works on one app. In contrast, large teams may use one Slack channel per app, or use different Slack channels for builds from pull requests, for workflows that distribute nightly builds, and so on.

To configure a workflow to send a build notification to a Slack channel:

1. Open a workflow in Xcode or App Store Connect.
2. Add a post-action by clicking the Add button and choosing Notify, or choose an existing Notify post-action.
3. Click the Add button in the post-action’s Slack section.
4. Choose a channel in the popover and click OK. If you’re a member of many Slack channels, filter the channels to find the one you’re looking for.
5. Configure any notification settings; for example, choose to only receive notifications for build failures, then save your changes.

> **Note**: If you configure Xcode Cloud to send build status notifications to a private Slack channel, Xcode Cloud redacts its name for team members who aren’t members of the private channel.

If you configure Xcode Cloud to send build status notifications to a private Slack channel, Xcode Cloud redacts its name for team members who aren’t members of the private channel.

## See Also

- [Configuring webhooks in Xcode Cloud](configuring-webhooks-in-xcode-cloud.md)
  Configure webhooks that connect Xcode Cloud to other services and tools.
- [Xcode Cloud webhook payload reference](webhook-payload.md)
  Review details of the webhook payload that Xcode Cloud sends, including the product, workflow, build, actions, results, and SCM metadata associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-slack)*