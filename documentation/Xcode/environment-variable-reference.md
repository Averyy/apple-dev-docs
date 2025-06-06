# Environment variable reference

**Framework**: Xcode

Review predefined environment variables you use in custom build scripts.

#### Overview

With custom workflows, you can tailor Xcode Cloud to your needs. When you create a custom workflow, you configure the temporary build environment Xcode Cloud uses, start conditions, actions, and other settings. However, you may need to perform custom tasks, for example, installing a third-party tool or uploading a build’s artifacts to your server. To achieve this, Xcode Cloud supports running custom shell scripts, referred to as .

Xcode Cloud includes a set of predefined environment variables that you can use to write flexible custom build scripts with advanced control flows. For example, access the `CI_XCODEBUILD_ACTION` variable in your script to determine which action is running and use this information to run a specific command. You can also use the absence of a variable to change your custom build script’s control flow.

> 💡 **Tip**: In addition to predefined environment variables, you can set custom environment variables in a workflow’s Environment section and access them in your custom build scripts or test actions.

For more information on using custom build scripts and accessing environment variables, see [`Writing custom build scripts`](writing-custom-build-scripts.md).

##### Variables That Are Always Available

The following environment variables are available every time Xcode Cloud starts a build, no matter which actions or start conditions you configure for a workflow:

> **Note**: Xcode Cloud builds your project using temporary build environments that use an HTTP proxy and makes the standard `HTTP_PROXY` and `HTTPS_PROXY` environment variables available. Many tools respect those variables and use them to change their settings.

##### Variables for Specific Start Conditions

The availability of the following environment variables depends on the workflow’s start condition you configure. For example, the `CI_PULL_REQUEST_NUMBER` variable is only available if the Pull Request Change start condition started the build.

###### Variable for Branch Changes

###### Variable for Tag Changes

###### Variable for Branch Changes and Tag Changes

###### Variables for Pull Request Changes

##### Variables for Specific Actions

The availability of the following environment variables depends on the action Xcode Cloud performs. For example, the `CI_ARCHIVE_PATH` variable is only available when Xcode Cloud performs an archive action.

###### Variables for Test Actions

> **Note**: Xcode Cloud makes all the environment variables for test actions available to the processes that execute your tests, known as . This includes environment variables set by the system as well as any custom environment variables you set in the Environment section of your workflow. When executing your test action, Xcode Cloud adds the prefix `TEST_RUNNER_` to each variable’s name, which is required by `xcodebuild` for the test runner process to access each variable by its original name. For more information on using the `TEST_RUNNER_` prefix on your environment variables when running `xcodebuild`, see the Environment Variables section of `xcodebuild`’s [`man page`](https://developer.apple.comx-man-page://1/xcodebuild).

###### Variables for Archive Actions

## See Also

- [Writing custom build scripts](writing-custom-build-scripts.md)
  Extend your Xcode Cloud workflows with custom build scripts that perform custom tasks or install additional tools.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/environment-variable-reference)*