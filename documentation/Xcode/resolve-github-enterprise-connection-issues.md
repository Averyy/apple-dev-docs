# Resolve GitHub Enterprise connection issues

**Framework**: Xcode

Verify that Xcode Cloud can access your GitHub Enterprise repository and fix configuration issues.

#### Overview

Xcode Cloud needs to have access to your Git repository to check out your code and build your app. You grant this access when you create your first workflow, or, in an enterprise context, your team’s administrator configures the connection for you before you start using Xcode Cloud.

If you work in a large team that uses GitHub Enterprise, you may have no control over the configuration of your team’s GitHub Enterprise setup. As a result, you may run into issues where Xcode Cloud can’t access your Git repository and can’t start builds. In this case, Xcode and App Store Connect display messages that indicate configuration or permission issues.

Common reasons for these issues are:

- The administrator of your GitHub Enterprise instance changed permissions; for example, permissions for the GitHub Enterprise app that Xcode Cloud uses to access your repository.
- The callback URL of your GitHub Enterprise instance changed.
- The GitHub Enterprise app that Xcode Cloud uses to connect to your repository received an update and requires permission updates.

Fixes for permission and configuration issues depend on your GitHub Enterprise instance, but common ways to re-enable Xcode Cloud to connect to your repository include:

- Visit your GitHub Enterprise team’s settings page and look for outstanding requested permission updates.
- Visit the settings page for the GitHub app that manages access to your Git repositories, and verify the callback URL. Additionally, verify that the configured permissions and events match those in the table and list below.

Required permissions:

| Type | Value |
| --- | --- |
| Checks | Read and write |
| Contents | Read-only |
| Metadata | Read-only |
| Pull Requests | Read-only |
| Statuses | Read and write |

Required events:

- Create
- Check Run
- Check Suite
- Delete
- Pull Request
- Pull Request Review
- Push
- Repository

As a last resort, you can disconnect Xcode Cloud from your GitHub Enterprise repository as described in [`Disconnect your Git repository in Xcode Cloud`](removing-your-project-from-xcode-cloud#Disconnect-your-Git-repository-in-Xcode-Cloud.md) and uninstall the app that guards access to your GitHub Enterprise repository as described in [`Remove personal access tokens or apps`](removing-your-project-from-xcode-cloud#Remove-personal-access-tokens-or-apps.md). However, you have to reconnect GitHub Enterprise to Xcode Cloud and configure access to each of your repositories on GitHub Enterprise — which may take a considerable amount of time if you have a lot of repositories and projects.

> ❗ **Important**: Make sure you don’t delete your Xcode Cloud data and workflows. If you do this, you will lose access to your workflows and build data, and you’ll have to configure Xcode Cloud workflows for your project again.

Make sure you don’t delete your Xcode Cloud data and workflows. If you do this, you will lose access to your workflows and build data, and you’ll have to configure Xcode Cloud workflows for your project again.

## See Also

- [Resolving common configuration and build issues](resolving-common-configuration-and-build-issues.md)
  Review common configuration and build issues and learn how you can resolve them.
- [Reporting feedback for Xcode Cloud](reporting-feedback-for-xcode-cloud.md)
  Provide feedback on issues you encounter when building with Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/resolve-github-enterprise-connection-issues)*