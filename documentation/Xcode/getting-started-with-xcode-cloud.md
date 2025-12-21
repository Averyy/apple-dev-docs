# Getting started with Xcode Cloud

**Framework**: Xcode

A quick start guide to getting your project set up with Xcode Cloud for continuous integration, development, and distribution.

#### Overview

Xcode Cloud is a continuous integration and delivery (CI/CD) system that combines the tools you use to create apps and frameworks for Apple platforms.

To onboard your project with Xcode Cloud, you:

1. Select your app or framework.
2. Decide on your first workflow.
3. Connect your Git repository to Xcode Cloud.
4. Create an app record if necessary.
5. Start your first build.

After adding your project to Xcode Cloud, you can customize your configuration as needed for your specific development and distribution needs.

For more information, see [`Setting up your project to use Xcode Cloud`](setting-up-your-project-to-use-xcode-cloud.md) and [`Configuring your first Xcode Cloud workflow`](configuring-your-first-xcode-cloud-workflow.md).

#### Before You Begin

Before you start using Xcode Cloud, you need to:

- Be a member of the Apple Developer Program. For information on joining the Developer program, see [`Distributing your app for beta testing and releases`](distributing-your-app-for-beta-testing-and-releases.md).
- Add your account to Xcode in Apple Accounts settings.
- Ensure that your app has a unique bundle identifier.
- Have permissions to do create an app record or create an app record yourself in App Store Connect (see [`Add a new app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app)).
- Have a remote Git repository with admin access.
- Push your latest project changes to the remote repository.

![A screenshot of the Accounts settings showing the Add Apple Account button.](https://docs-assets.developer.apple.com/published/f8232d11804a53940d490c67de7d2b19/xcode-cloud-add-account%402x.png)

#### Configure Xcode Cloud for Your Project

To use Xcode Cloud with your project:

1. Open your project in Xcode.
2. In the Report navigator, click the Cloud tab.
3. Click the Get Started button that appears below.

![A screenshot showing the Cloud tab selected in the Report navigator on the left and information about Xcode Cloud and a Get Started button underneath.](https://docs-assets.developer.apple.com/published/f63e1eeec9d4cf869a9285307adf65b4/xcode-cloud-get-started%402x.png)

#### Add Your Project to Xcode Cloud

In the sheet that appears after clicking Get Started, find your app or framework:

1. Select your app or framework  from the list that Xcode detects.
2. Select the team for the app or framework, if it isn’t already selected.
3. Click Next.

![A screenshot showing a list of apps and frameworks to select from in the sheet that appears.](https://docs-assets.developer.apple.com/published/8879e7e7fb9410d312c6f680b2e79015/xcode-cloud-add-your-app%402x.png)

> **Note**: If you don’t have a remote Git repository, Xcode offers to create a local repository for you.

#### Review the Suggested Workflow

In the next sheet, Xcode shows you a default workflow that:

- Starts a build on every change to your main branch.
- Uses the latest macOS and Xcode versions.
- Archives your app or framework.

To accept the default workflow, click Next. Otherwise, click Edit Workflow.

![A screenshot showing the sheet where you review the default start conditions.](https://docs-assets.developer.apple.com/published/818f5bf3bce5200d46759e34bc78c770/xcode-cloud-review-workflow%402x.png)

> 💡 **Tip**: Create a basic workflow at first that you can customize later.

For more information on choosing start conditions, see [`Configuring start conditions`](configuring-start-conditions.md).

#### Grant Xcode Cloud Access to Your Git Repository

Grant access to your git repository to allow Xcode Cloud to automatically build and test your code when you make changes:

1. Click Grant Access.
2. In the browser window that appears, follow the instructions to authorize Xcode Cloud access to your Git repository.
3. If necessary, sign in to your App Store Connect account and follow the steps that appear.
4. Follow the instructions in the browser to finish granting access to your Git repository.
5. In Xcode, click Next to add your project’s Git repository to Xcode Cloud.

![A screenshot showing the remote repository details that Xcode Cloud needs access to.](https://docs-assets.developer.apple.com/published/72846ef8c5ffa298b3b386f7d72ddd96/xcode-cloud-grant-access%402x.png)

For Git repository-specific instructions, see [`Source code management setup`](source-code-management-setup.md).

#### Create an App Record

Xcode Cloud uses an existing app record that matches your bundle identifier, if available. Otherwise, Xcode Cloud creates a new app record for you.

In the Create App on App Store Connect dialog that appears:

1. Verify that the app name and bundle identifier are correct.
2. Enter a SKU and choose a primary language.
3. Click Complete.

![A screenshot showing the app record details before Xcode creates it in your App Store Connect account.](https://docs-assets.developer.apple.com/published/25afd7d8b945b5d8d6ec6a7e3f0a4394/xcode-cloud-create-app-record%402x.png)

> ❗ **Important**: If your app name or bundle identifier aren’t unique, change them now and push your changes to your remote Git repository before continuing.

#### Start Your First Build

Now let Xcode Cloud build your app or framework as the final onboarding step.

1. In the Start Build dialog, confirm the branch that you want Xcode Cloud to build your project from.
2. Click Start Build.

![A screenshot showing the pop-up menu that you choose a branch in your repository from.](https://docs-assets.developer.apple.com/published/e1a8271cb6b7f3b06d38be01b7e3f836/xcode-cloud-start-build%402x.png)

##### Next Steps

View the progress of your build in the Report navigator.

1. If necessary, click the Cloud tab.
2. To customize the workflow, Control-click your app or framework and choose Manage Workflows (Integrate > Manage Worflows).
3. If you encounter build issues, see [`Resolving common configuration and build issues`](resolving-common-configuration-and-build-issues.md) for tips.

![A screenshow showing the Report navigator with the Cloud tab selected on the left and the status of an Xcode Cloud build on the right.](https://docs-assets.developer.apple.com/published/40be6c99c9194c46e59171daa5820b28/xcode-cloud-report-navigator%402x.png)

Similarly, you can view builds and manage workflows in App Store Connect if you prefer.

## See Also

- [About continuous integration and delivery with Xcode Cloud](about-continuous-integration-and-delivery-with-xcode-cloud.md)
  Learn how continuous integration and delivery with Xcode Cloud helps you create high-quality apps and frameworks.
- [Setting up your project to use Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md)
  Review account, project, and source control requirements before configuring your project or workspace to use Xcode Cloud.
- [Configuring your first Xcode Cloud workflow](configuring-your-first-xcode-cloud-workflow.md)
  Set up your project or workspace to use Xcode Cloud and adopt continuous integration and delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/getting-started-with-xcode-cloud)*