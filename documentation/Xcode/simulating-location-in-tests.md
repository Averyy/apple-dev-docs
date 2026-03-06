# Simulating location in tests

**Framework**: Xcode

Improve test reliability and coverage when working with location-based code.

#### Overview

Automated tests are most reliable when you control all of the inputs to the code under test. When testing code that works with location APIs, use specific values for coordinates and locations so that the outcome of the tests doesn’t depend on the physical location of the device running the tests.

Test your code with different simulated locations to improve the test coverage of your location-handling code.

##### Simulate a Static Device Location

If your app uses [`Core Location`](https://developer.apple.com/documentation/CoreLocation) or [`MapKit`](https://developer.apple.com/documentation/MapKit), the app’s behavior under test can depend on the device’s location. Configure your test plan to simulate a predetermined location so tests run with repeatable inputs. To set a simulated location in a test plan, follow these steps:

1. Open Xcode.
2. Choose Product > Test Plan > Edit Test Plan.
3. In the test plan editor pane, choose Configuration.
4. Under Localization, click Simulated Location and choose a location from the menu.

For more information on configuring test plans, see [`Improving code assessment by organizing tests into test plans`](organizing-tests-to-improve-feedback.md).

> **Note**:  When you set a simulated location in Xcode, the location changes only for code running in the test bundle. UI automation tests communicate with your app running as a separate process, so in those tests, your app doesn’t use the simulated location. To simulate location in a UI automation test, see the “Set a simulated location for UI automation” section below.

##### Replay a Previously Recorded Journey

Test features of your app that work with changes to the device’s location by setting the simulated location to a GPX file. Xcode uses the GPX file to replay a journey while your tests are running, updating the simulated location, elevation, and velocity of the device to replicate the recorded journey. To add a GPX file to your workspace, follow these steps:

1. Open Xcode.
2. Choose Product > Test Plan > Edit Test Plan.
3. In the test plan editor pane, choose Configuration.
4. Under Localization, click Simulated Location and choose Add GPX File to Workspace.
5. Navigate to your GPX file and click Add.

Xcode uses the added GPX file to simulate locations in tests. You can add multiple GPX files and choose between them using the Simulated Location setting in the test plan configuration.

##### Construct Locations for Unit Tests

When testing your app’s location-handling logic, you don’t need to use [`CLLocationManager`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager) or get the device’s location. You can construct instances of [`CLLocationCoordinate2D`](https://developer.apple.com/documentation/CoreLocation/CLLocationCoordinate2D) with known values for the coordinate’s latitude and longitude in the test. Pass these instances to the code under test, and validate that your code behaves as expected for the given values.

##### Set a Simulated Location for Ui Automation

In your UI automation tests, update the simulated device location by setting the shared [`XCUIDevice`](https://developer.apple.com/documentation/XCTest/XCUIDevice) location to an instance of [`XCUILocation`](https://developer.apple.com/documentation/XCTest/XCUILocation).

```swift
import XCTest
import CoreLocation

final class SampleAppTests: XCTestCase {

  func testExample() throws {
    XCUIDevice.shared.location = XCUILocation(location: CLLocation(latitude: 37.334886, longitude: -122.008988))
	// Launch your app and run the test.
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/simulating-location-in-tests)*