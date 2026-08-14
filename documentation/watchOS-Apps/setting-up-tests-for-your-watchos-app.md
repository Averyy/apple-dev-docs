# Setting up tests for your watchOS app

**Framework**: watchOS apps

Configure your watch-only project with unit tests and user interface tests.

#### Overview

Xcode offers unit and user interface tests to use while building your watchOS app. Add them to your project to confirm that your features work as expected, prevent performance regressions, and validate user interaction flows.

##### Add a Test Target to the Project

Add a unit test or UI test target to your existing watch-only watchOS Xcode project by choosing File > New > Target to open the template selection dialog. Alternatively, select the project in the Project navigator, select the General tab, and click the Add a Target button (+) at the bottom of the Targets area.

Xcode presents the template selection dialog. Select watchOS, and then select the watchOS UI Testing Bundle or the watchOS Unit Testing Bundle option in the Test section, and click Next.

![An Xcode screenshot showing the template selection dialog with the watchOS platform in a selected state. The dialog contains three horizontal sections: Test, Application, and Framework & Library. A rectangle surrounds the watchOS UI Testing Bundle and watchOS Unit Testing Bundle options in the Test section. The watchOS Unit Testing Bundle option is in a selected state.](/images/com.apple.watchOS-Apps/setting-up-tests-for-your-watchos-app-1@2x.png)

Specify a name for the test target, and then choose the WatchKit Extension option as the target if you’re adding unit tests, or the WatchKit App option if you’re adding UI tests.

![An Xcode screenshot showing the available options for a new target, which include entering a product name and organization identifier, and choosing a team, programming language, project, and target to test. The WatchKit Extension option displays as the target to test.](/images/com.apple.watchOS-Apps/setting-up-tests-for-your-watchos-app-2@2x.png)

Xcode adds the target and template files to your project, and creates a new scheme to run your tests. Select the new scheme, named [*Project Name*] `WatchKit ExtensionTests`, from the list of schemes in Xcode’s toolbar, and choose Edit Scheme.

Confirm the selected executable is [*Project Name*] `WatchKit App.app`. If not, choose it and click Close.

![A screenshot of an Xcode scheme editor showing the Info pane for the selected Run action. Options available for selection are: Build Configuration, Executable, Watch Interface, and Launch. The WatchKit App option displays as the executable option.](/images/com.apple.watchOS-Apps/setting-up-tests-for-your-watchos-app-3@2x.png)

##### Make the Extension Code Visible in Unit Tests

When you add a unit test file to your test target, your watch extension code isn’t visible to your tests by default. Add an `@testable import` declaration at the top of your test file, specifying your watch extension name, to make your extension code testable.

![An image of the first three lines of code in a sample test file that Xcode generates. A rectangle surrounds the @testable import declaration on the second line.](/images/com.apple.watchOS-Apps/setting-up-tests-for-your-watchos-app-4@2x.png)

##### Switch Schemes to Run Tests

If you try to run your tests before switching to the new test scheme, Xcode lets you know that the current scheme isn’t set up for testing.

![A dialog that indicates the active scheme doesn’t include the tests you’re trying to run, and asks if you would like to configure the scheme. There are two buttons: the Edit Scheme button and the Cancel button.](/images/com.apple.watchOS-Apps/setting-up-tests-for-your-watchos-app-5@2x.png)

Click Cancel and select the new test scheme from the list of schemes in Xcode’s toolbar, and choose Product > Test to run your tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/setting-up-tests-for-your-watchos-app)*