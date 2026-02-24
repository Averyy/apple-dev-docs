# Grouping Tests into Substeps with Activities

**Framework**: XCTest

Simplify test reports by creating activities that organize substeps within complex test methods.

#### Overview

Use activities to break longer test methods, such as UI tests and integration tests, into smaller named substeps.

Each activity wraps a block of code, giving the code a name. You can nest and call activities within other activities. Xcode test reports organize results by activity name, making test reports for complex, multistep tests easier to understand.

For long test methods, especially in UI tests that contain lots of steps, simplify your test methods by refactoring them into utility methods or substeps with activities.

##### Organize Long Test Methods Into Substeps

Identify the substeps that you want to group into named activities. For example, you might break down a login UI test into three substeps: opening the login window, entering a password, and closing the login window. Then, create named activities for each substep you identify.

**Swift**:

```swift
func testLogin() throws {
    openLoginWindow()
    enterPassword(for: .member)
    closeLoginWindow()
}

func openLoginWindow() {
    XCTContext.runActivity(named: "Open login window") { activity in
        let loginButton = app.buttons["Login"]
        
        XCTAssertTrue(loginButton.exists, "Login button is missing.")
        XCTAssertTrue(loginButton.isHittable, "Login button is not hittable.")
        XCTAssertFalse(app.staticTexts["Logged In"].exists, "Logged In label is visible and should not be.")

        loginButton.tap()
        
        let loginLabel = app.staticTexts["Login:"]
        XCTAssertTrue(loginLabel.waitForExistence(timeout: 3.0), "Login label is missing.")
    }
}

func enterPassword(for userType: TestUserType) {
    XCTContext.runActivity(named: "Enter password") { activity in
        let userNameTextField = app.textFields["user name"]
        userNameTextField.tap()
        userNameTextField.typeText(userType.userName)

        let passwordSecureTextField = app.secureTextFields["password"]
        passwordSecureTextField.tap()
        passwordSecureTextField.typeText(userType.password)
        
        // Dismiss keyboard.
        app.children(matching: .window).firstMatch.tap()
    }
}

func closeLoginWindow() {
    XCTContext.runActivity(named: "Close login window") { activity in
        let submitLoginButton = app.buttons["Submit"]
        XCTAssertTrue(submitLoginButton.exists, "Submit button is missing.")
        XCTAssertTrue(submitLoginButton.isHittable, "Submit button is not hittable.")
        submitLoginButton.tap()
        XCTAssertTrue(app.staticTexts["Logged In"].waitForExistence(timeout: 3.0), "Logged In label is missing.")
    }
}

```

**Objective-C**:

```objc
- (void)testLogin {
    [self openLoginWindow];
    [self enterPasswordAndUserName:@"member"];
    [self closeLoginWindow];
}

- (void)openLoginWindow {
    [XCTContext runActivityNamed:@"Open login window" block:^(id<XCTActivity> activity) {
        XCUIElement *loginButton = self.app.buttons[@"Login"];
        XCTAssertTrue(loginButton.exists, @"Login button is missing.");
        XCTAssertTrue(loginButton.isHittable, @"Login button is not hittable.");
        XCTAssertFalse(self.app.staticTexts[@"Logged In"].exists, @"Logged In label is visible and should not be.");
        [loginButton tap];
        
        XCUIElement *loginLabel = self.app.staticTexts[@"Login:"];
        BOOL loginLabelAppeared = [loginLabel waitForExistenceWithTimeout:3.0];
        XCTAssertTrue(loginLabelAppeared, @"Login label is missing.");
    }];
}

- (void)enterPasswordAndUserName:(NSString *)userName {
    [XCTContext runActivityNamed:@"Enter password" block:^(id<XCTActivity> activity) {
        XCUIElement *userNameTextField = self.app.textFields[@"user name"];
        [userNameTextField tap];
        [userNameTextField typeText:userName];
        
        XCUIElement *passwordSecureTextField = self.app.secureTextFields[@"password"];
        [passwordSecureTextField tap];
        [passwordSecureTextField typeText:@"password"];
        
        //Dismiss keyboard.
        [[[self.app childrenMatchingType:XCUIElementTypeWindow] firstMatch] tap];
    }];
}

- (void)closeLoginWindow {
    [XCTContext runActivityNamed:@"Close login window" block:^(id<XCTActivity> activity) {
        XCUIElement *submitLoginButton = self.app.buttons[@"Submit"];
        XCTAssertTrue(submitLoginButton.exists, @"Submit button is missing.");
        XCTAssertTrue(submitLoginButton.isHittable, @"Submit button is not hittable.");
        [submitLoginButton tap];

        BOOL loggedInLabelAppeared = [self.app.staticTexts[@"Logged In"] waitForExistenceWithTimeout:3.0];
        XCTAssertTrue(loggedInLabelAppeared, @"Logged In label is missing.");
    }];
}

```

Activities run against the current testing context, represented by [`XCTContext`](xctcontext.md). To run a block of code as an activity, call the [`runActivityNamed:block:`](xctcontext/runactivitynamed:block:.md) class method on `XCTContext`, passing your test code as the block to execute.

##### Build Utility Methods From Common Test Substeps

Convert common test substeps into self-contained utility methods for reuse in multiple tests with activities. For example, if you have three UI tests that each require the user to be logged in, extract the login process into a utility method that wraps the process inside an activity called `Login`, and call the utility method from within each test method. The login activity appears in the Xcode test report for each test method that calls it.

**Swift**:

```swift
func testAdminLoginFeatures() throws {
    let loginResult = login(for: .admin)
    try XCTAssertTrue(loginResult.get() == .admin)
    
    XCTAssertTrue(app.buttons["Admin Features"].exists, "Missing Admin Features button.")
    XCTAssertFalse(app.buttons["Member Features"].exists, "Member Features button is visible and should not be.")
}

func testMemberLoginFeatures() throws {
    let loginResult = login(for: .member)
    try XCTAssertTrue(loginResult.get() == .member)
    
    XCTAssertFalse(app.buttons["Admin Features"].exists, "Admin Features button is visible and should not be.")
    XCTAssertTrue(app.buttons["Member Features"].exists, "Missing Member Features button.")
}

func testGuestLoginFeatures() throws {
    let loginResult = login(for: .guest)
    
    switch loginResult {
    case .success:
        XCTAssertFalse(app.buttons["Admin Features"].exists, "Admin Features button is visible and should not be.")
        XCTAssertFalse(app.buttons["Member Features"].exists, "Member Features button is visible and should not be.")
    case .failure(let error):
        throw XCTSkip("Guest logins are still not working, skip this test. Error was: \(error)")
    }
}

func login(for userType: TestUserType) -> Result<TestUserType, Error> {
    return XCTContext.runActivity(named: "Login") { activity in
        performLoginUITests(for: userType)
        
        guard app.staticTexts["Logged In"].exists else {
            let screenshot = app.windows.firstMatch.screenshot()
            let attachment = XCTAttachment(screenshot: screenshot)
            attachment.lifetime = .keepAlways
            activity.add(attachment)
            return .failure(TestLoginError.invalidLogin)
        }
        return .success(userType)
    }
}

```

**Objective-C**:

```objc
- (void)testAdminLoginFeatures {
    BOOL loginResult = [self loginForUserName:@"admin"];
    XCTAssertTrue(loginResult);
    
    XCTAssertTrue(self.app.buttons[@"Admin Features"].exists, @"Missing Admin Features button.");
    XCTAssertFalse(self.app.buttons[@"Member Features"].exists, @"Member Features button is visible and should not be.");
}

- (void)testMemberLoginFeatures {
    BOOL loginResult = [self loginForUserName:@"member"];
    XCTAssertTrue(loginResult);

    XCTAssertFalse(self.app.buttons[@"Admin Features"].exists, @"Admin Features button is visible and should not be.");
    XCTAssertTrue(self.app.buttons[@"Member Features"].exists, @"Missing Member Features button.");
}

- (void)testGuestLoginFeatures {
    BOOL loginResult = [self loginForUserName:@"guest"];
    if (loginResult == YES) {
        XCTAssertFalse(self.app.buttons[@"Admin Features"].exists, @"Admin Features button is visible and should not be.");
        XCTAssertFalse(self.app.buttons[@"Member Features"].exists, @"Member Features button is visible and should not be.");
    } else {
        XCTSkip(@"Guest logins are still not working, skip this test.");
    }
}

- (BOOL)loginForUserName:(NSString *) userName {
    __block BOOL loginSuccessful = NO;
    [XCTContext runActivityNamed:@"Login" block:^(id<XCTActivity> activity) {
        [self performLoginUITestsForUserName:userName];
        loginSuccessful = self.app.staticTexts[@"Logged In"].exists;
        if (!loginSuccessful) {
            XCUIScreenshot *screenshot = [self.app.windows.firstMatch screenshot];
            XCTAttachment *attachment = [XCTAttachment attachmentWithScreenshot:screenshot];
            attachment.lifetime = XCTAttachmentLifetimeKeepAlways;
            [activity addAttachment:attachment];
        }
    }];
    return loginSuccessful;
}

```

If the login fails, the login activity adds a screenshot as an attachment for later investigation. For more information, see [`Adding Attachments to Tests, Activities, and Issues`](adding-attachments-to-tests-activities-and-issues.md).

You can use `XCTContext` anywhere within your test target, not just within test methods on an [`XCTestCase`](xctestcase.md) subclass. This enables you to define activities in your own utility code, such as in custom methods on subclasses of [`XCUIApplication`](https://developer.apple.com/documentation/XCUIAutomation/XCUIApplication) or [`XCUIElement`](https://developer.apple.com/documentation/XCUIAutomation/XCUIElement).

## See Also

- [class XCTContext](xctcontext.md)
  A proxy for the current testing context.
- [protocol XCTActivity](xctactivity.md)
  A named substep of a test method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/grouping-tests-into-substeps-with-activities)*