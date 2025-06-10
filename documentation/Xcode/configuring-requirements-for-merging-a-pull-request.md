# Configuring requirements for merging a pull request

**Framework**: Xcode

Protect stable branches by requiring a successful Xcode Cloud build or action before it’s possible to merge a pull request.

#### Overview

When you configure an Xcode Cloud workflow that starts a new build for every change to a pull request (PR), Xcode Cloud reports the build status on your source code management (SCM) provider’s webpage for a PR. As a result, you can identify issues that changes in the PR caused. However, the build status doesn’t prevent you from merging a PR with a failed Xcode Cloud build.

To prevent merging PRs that contain errors, [`Bitbucket Cloud`](https://developer.apple.comhttps://bitbucket.org), [`Bitbucket Server`](https://developer.apple.comhttps://bitbucket.org/product/enterprise), [`GitHub`](https://developer.apple.comhttps://github.com), and [`GitHub Enterprise`](https://developer.apple.comhttps://github.com/enterprise) allow you to configure requirements that a PR must meet before it’s possible to merge it. Xcode Cloud supports these branch protection features. You can require that an entire Xcode Cloud build must succeed before it’s possible to merge a PR, or you can require that a specific Xcode Cloud action must succeed.

The user interface for configuring requirements for PRs depends on the SCM provider:

- [`Bitbucket Cloud`](https://developer.apple.comhttps://bitbucket.org) and [`Bitbucket Server`](https://developer.apple.comhttps://bitbucket.org/product/enterprise) refer to their branch protection features as . For more information about Bitbucket code insights and configuring requirements for PRs, see [`Bitbucket documentation`](https://developer.apple.comhttps://support.atlassian.com/bitbucket-cloud/docs/code-insights/).
- [`GitHub`](https://developer.apple.comhttps://github.com) and [`GitHub Enterprise`](https://developer.apple.comhttps://github.com/enterprise) refer to their branch protection features as . For more information about GitHub status checks and configuring requirements for PRs, see [`GitHub documentation`](https://developer.apple.comhttps://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks).
- [`GitLab`](https://developer.apple.comhttps://gitlab.com) and [`self-managed GitLab instances`](https://developer.apple.comhttps://about.gitlab.com/install) don’t come with branch protection features that prevent merging PRs with errors. Instead, they only display build status information. This is a limitation of GitLab and self-managed GitLab instances and not limited to Xcode Cloud.

> **Note**: To configure requirements for PRs, you need the same permission or role that you need to initially connect Xcode Cloud to your Git repository. For information about required permissions and roles, see [`Use a remote source control repository`](setting-up-your-project-to-use-xcode-cloud#Use-a-remote-source-control-repository.md).

#### Configure Requirements

To require a successful Xcode Cloud build or action before it’s possible to merge a PR:

1. Configure a workflow that starts a new build for changes to a PR. For more information, see [`Start builds for changes to a pull request`](configuring-start-conditions#Start-builds-for-changes-to-a-pull-request.md).
2. Navigate to the configuration section of your SCM provider’s website, and follow the instructions to add requirements for PRs.

For example, configure an Xcode Cloud workflow that starts a build for each change to a PR and performs a test and an archive action. On your SCM provider’s website, require a successful Xcode Cloud build to ensure that the target branch only receives verified changes. Alternatively, require a successful archive action and allow merging a PR even if the test action fails. A common use case for this configuration is during feature development when you consider it OK to merge PRs that target a feature branch even if they cause unit tests to fail.

## See Also

- [Source code management setup](source-code-management-setup.md)
  Allow Xcode Cloud to access your Git repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-requirements-for-merging-a-pull-request)*