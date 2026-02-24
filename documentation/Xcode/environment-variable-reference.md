# Environment variable reference

**Framework**: Xcode

Review predefined environment variables you use in custom build scripts.

#### Overview

With custom workflows, you can tailor Xcode Cloud to your needs. When you create a custom workflow, you configure the temporary build environment Xcode Cloud uses, start conditions, actions, and other settings. However, you may need to perform custom tasks, for example, installing a third-party tool or uploading a build’s artifacts to your server. To achieve this, Xcode Cloud supports running custom shell scripts, referred to as *custom build scripts*.

Xcode Cloud includes a set of predefined environment variables that you can use to write flexible custom build scripts with advanced control flows. For example, access the `CI_XCODEBUILD_ACTION` variable in your script to determine which action is running and use this information to run a specific command. You can also use the absence of a variable to change your custom build script’s control flow.

> 💡 **Tip**: In addition to predefined environment variables, you can set custom environment variables in a workflow’s Environment section and access them in your custom build scripts or test actions.

For more information on using custom build scripts and accessing environment variables, see [`Writing custom build scripts`](writing-custom-build-scripts.md).

##### Variables That Are Always Available

The following environment variables are available every time Xcode Cloud starts a build, no matter which actions or start conditions you configure for a workflow:

- **`CI`**: A Boolean value that evaluates to `TRUE` when the custom build script runs in Xcode Cloud. Use it to only run the build script when Xcode Cloud builds your project or workspace. See also `CI_XCODE_CLOUD`.
- **`CI_BUILD_ID`**: A string that uniquely identifies the current build, for example, `12345678-ABCD-DEFG-1234-012345ABCDEF`.
- **`CI_BUILD_NUMBER`**: The number of the current build, for example, `42`.
- **`CI_BUILD_URL`**: A URL to the Xcode Cloud build in App Store Connect.
- **`CI_BUNDLE_ID`**: The bundle ID of the product, for example, `com.example.appname`.
- **`CI_COMMIT`**: The Git commit hash that Xcode Cloud uses for the current build.
- **`CI_DERIVED_DATA_PATH`**: The path to the directory that contains your project’s derived data.
- **`CI_PRIMARY_REPOSITORY_PATH`**: The location of the source code in the temporary build environment cloned from the primary repository specified in the workflow, for example, `/Volumes/workspace/repository`.
- **`CI_PRODUCT`**: The name of the workflow’s product.
- **`CI_PRODUCT_ID`**: A string that uniquely identifies the product, for example, `12345678-ABCD-DEFG-1234-012345ABCDEF`. Use it to distinguish between products in the same project or workspace.
- **`CI_PRODUCT_PLATFORM`**: The platform (`iOS`, `macOS`, `tvOS`, or `watchOS`) for the current action.
- **`CI_PROJECT_FILE_PATH`**: The path to the Xcode project or workspace in the temporary build environment.
- **`CI_START_CONDITION`**: The start condition that started the build. Available values are `manual`, `manual_rebuild`, `push`, `pr_open`, `pr_update`, and `schedule`.
- **`CI_TEAM_ID`**: The ID of your Apple Development team, for example, `ABCDE12345`.
- **`CI_WORKFLOW`**: The name of the workflow, for example, `Default Workflow`. Use this variable to run commands only for a specific workflow.
- **`CI_WORKFLOW_ID`**: A string that uniquely identifies the workflow, for example, `12345678-ABCD-DEFG-1234-012345ABCDEF`.
- **`CI_WORKSPACE_PATH`**: The location of the workspace used for cloning source code and storing artifacts, for example, `/Volumes/workspace`.
- **`CI_XCODE_CLOUD`**: A Boolean value that evaluates to `TRUE` when the custom build script runs in Xcode Cloud. Use it to only run the script content when Xcode Cloud builds your project or workspace.
- **`CI_XCODE_PROJECT`**: The name of the Xcode project or workspace.
- **`CI_XCODE_SCHEME`**: The scheme that the current action uses.
- **`CI_XCODEBUILD_ACTION`**: The `xcodebuild` command that Xcode Cloud is about to perform. Possible values are `analyze`, `archive`, `build`, `build-for-testing`, and `test-without-building`.
- **`CI_XCODEBUILD_EXIT_CODE`**: The exit code of the `xcodebuild` command. This variable is available after Xcode Cloud runs an action’s corresponding `xcodebuild` command. An exit code of `0` indicates that the `xcodebuild` command succeeded.

> **Note**: Xcode Cloud builds your project using temporary build environments that use an HTTP proxy and makes the standard `HTTP_PROXY` and `HTTPS_PROXY` environment variables available. Many tools respect those variables and use them to change their settings.

##### Variables for Specific Start Conditions

The availability of the following environment variables depends on the workflow’s start condition you configure. For example, the `CI_PULL_REQUEST_NUMBER` variable is only available if the Pull Request Change start condition started the build.

###### Variable for Branch Changes

- **`CI_BRANCH`**: The name of the source branch that Xcode Cloud checked out for the current build, for example, `main`.

###### Variable for Tag Changes

- **`CI_TAG`**: The name of the tag that Xcode Cloud checked out for the current build, for example, `release-1.1`.

###### Variable for Branch Changes and Tag Changes

- **`CI_GIT_REF`**: The canonical Git reference that contains the `CI_COMMIT`, for example, `refs/heads/bug-fix` for a build from the `bug-fix` branch and `refs/tags/release-1.0` from the `release-1.0` tag.

###### Variables for Pull Request Changes

- **`CI_PULL_REQUEST_HTML_URL`**: The URL to the pull request’s website.
- **`CI_PULL_REQUEST_NUMBER`**: The pull request’s number, for example, `42`.
- **`CI_PULL_REQUEST_SOURCE_BRANCH`**: The pull request’s source branch, for example, `feature/feature-12345`.
- **`CI_PULL_REQUEST_SOURCE_COMMIT`**: The Git commit hash of a pull request’s source. It’s the same value as `CI_COMMIT`.
- **`CI_PULL_REQUEST_SOURCE_REPO`**: The full name of a pull request’s source repository, for example, `example/fork-of-example-framework`. If the pull request involves only one repository, the variable’s value is the same as `CI_PULL_REQUEST_TARGET_REPO`.
- **`CI_PULL_REQUEST_TARGET_BRANCH`**: The pull request’s target branch, for example, `main`.
- **`CI_PULL_REQUEST_TARGET_COMMIT`**: The most recent Git commit hash of the pull request’s target branch. The CI service tests your changes against the merge of `CI_PULL_REQUEST_TARGET_COMMIT` and `CI_PULL_REQUEST_SOURCE_COMMIT`.
- **`CI_PULL_REQUEST_TARGET_REPO`**: The full name of the pull request’s target repository, for example, `example/original-repository-of-example-framework`. If the pull request involves only one repository, the variable’s value is the same as `CI_PULL_REQUEST_SOURCE_REPO`.

##### Variables for Specific Actions

The availability of the following environment variables depends on the action Xcode Cloud performs. For example, the `CI_ARCHIVE_PATH` variable is only available when Xcode Cloud performs an archive action.

###### Variables for Test Actions

- **`CI_RESULT_BUNDLE_PATH`**: The path to the test action’s result bundle (`.xcresult`).
- **`CI_TEST_DESTINATION_DEVICE_TYPE`**: The device type of the simulated device you choose as the test action’s destination, for example, `iPhone 11`.
- **`CI_TEST_DESTINATION_RUNTIME`**: The OS version of the simulated device you choose as the test action’s destination, for example, `iOS 13.0`.
- **`CI_TEST_DESTINATION_UDID`**: A string that uniquely identifies the simulated device you choose as the test action’s destination.
- **`CI_TEST_PLAN`**: The name of the test plan that the test action uses. This variable is only available if you use test plans.
- **`CI_TEST_PRODUCTS_PATH`**: The path to the directory that contains your project’s test products that Xcode Cloud creates.

> **Note**: Xcode Cloud makes all the environment variables for test actions available to the processes that execute your tests, known as *test runners*. This includes environment variables set by the system as well as any custom environment variables you set in the Environment section of your workflow. When executing your test action, Xcode Cloud adds the prefix `TEST_RUNNER_` to each variable’s name, which is required by `xcodebuild` for the test runner process to access each variable by its original name. For more information on using the `TEST_RUNNER_` prefix on your environment variables when running `xcodebuild`, see the Environment Variables section of `xcodebuild`’s [`man page`](https://developer.apple.comx-man-page://1/xcodebuild).

###### Variables for Archive Actions

- **`CI_AD_HOC_SIGNED_APP_PATH`**: The path to an exported archive that’s code-signed for Ad Hoc distribution.
- **`CI_APP_STORE_SIGNED_APP_PATH`**: The path to an exported archive that’s code-signed for TestFlight distribution and eligible for release on the App Store.
- **`CI_ARCHIVE_PATH`**: The path to the exported app archive that Xcode Cloud creates when it runs an archive action.
- **`CI_DEVELOPMENT_SIGNED_APP_PATH`**: The path to an exported app archive that’s code-signed for development distribution.
- **`CI_DEVELOPER_ID_SIGNED_APP_PATH`**: The path to an exported app archive that’s code-signed using the Developer ID certificate. Use Developer ID signing only for Mac apps distributed outside the Mac App Store. For more information, see [`Developer ID`](https://developer.apple.comhttps://developer.apple.com/developer-id/).

## See Also

- [Writing custom build scripts](writing-custom-build-scripts.md)
  Extend your Xcode Cloud workflows with custom build scripts that perform custom tasks or install additional tools.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/environment-variable-reference)*