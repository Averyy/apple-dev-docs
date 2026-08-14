# Distributing your Xcode Cloud builds through TestFlight

**Framework**: Xcode

Create a TestFlight distribution workflow for internal testers.

#### Overview

When you’re ready to get feedback, use Xcode Cloud to deliver builds to TestFlight. Distributing your app with TestFlight lets people try new features and report bugs. When you’re ready to distribute your app through the App Store, you can use Xcode Cloud to deliver builds too.

#### Before You Begin

Before you create a distribution workflow, set up Xcode Cloud to build and test your app for development. For more information, see [`Getting started with Xcode Cloud`](getting-started-with-xcode-cloud.md).

If you don’t have an app record in App Store Connect, make sure that your Apple Developer Program account has permission to create app records before you set up distribution. To join the Apple Developer Program, see [`Become a member`](https://developer.apple.comhttps://developer.apple.com/programs/enroll/).

#### Create an App Record

To get started, click the Cloud tab in the Report navigator. Control-click your product and choose Set Up Distribution from the context menu.

If an app record exists in your account that matches your bundle identifier, Xcode Cloud uses it. Otherwise, Xcode Cloud creates a new app record for you if your app name and bundle identifier are unique.

If the Create App sheet appears, verify that the team, app name, and bundle identifier are correct. If an error message appears because another app already uses your app name, enter a new app name in the Name text field. Change any other information in the sheet if necessary and click Create.

![A screenshot of the Create App sheet showing the app record details including the app name and bundle ID with the Create button below.](/images/com.apple.Xcode/xcode-cloud-create-app-record@2x.png)

If the Confirm Existing App sheet appears instead, verify that the app name and bundle identifier are correct and click Next.

Xcode Cloud creates a workflow for getting started with internal TestFlight distribution by default. If you want to add an internal TestFlight post-action to your workflow, create an internal tester group in App Store Connect first. For more information, see [`Add internal testers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-a-beta-version/add-internal-testers).

Alternatively, create an app record in App Store Connect before you set up distribution in Xcode. For more information, see [`Add a new app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app).

#### Start Your First Build

Then, start a build of your app or framework with Xcode Cloud.

1. In the next sheet, confirm which branch Xcode Cloud uses to build your product.
2. Click Start Build.

![A screenshot of the Set Up for Distribution sheet showing the pop-up menu that you choose a branch in your repository from and a Start Build button below.](/images/com.apple.Xcode/xcode-cloud-start-build@2x.png)

Xcode Cloud archives the build and uploads it to App Store Connect for you.

#### View Build Progress

As the final step, view the build in the Cloud pane of the Report navigator. To view distribution builds and manage workflows in App Store Connect instead, click your app, and then click the Xcode Cloud tab. In the sidebar, navigate to your builds, workflows, and settings.

## See Also

- [Getting started with Xcode Cloud](getting-started-with-xcode-cloud.md)
  Use Xcode Cloud to build and test your app in the cloud during development.
- [About continuous integration and delivery with Xcode Cloud](about-continuous-integration-and-delivery-with-xcode-cloud.md)
  Learn how continuous integration and delivery with Xcode Cloud helps you create high-quality apps and frameworks.
- [Setting up your project to use Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md)
  Review account, project, and source control requirements before configuring your project or workspace to use Xcode Cloud.
- [Configuring your first Xcode Cloud workflow](configuring-your-first-xcode-cloud-workflow.md)
  Set up your project or workspace to use Xcode Cloud and adopt continuous integration and delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/distributing-your-xcode-cloud-builds-through-testflight)*