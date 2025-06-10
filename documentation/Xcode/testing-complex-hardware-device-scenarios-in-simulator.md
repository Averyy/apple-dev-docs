# Testing complex hardware device scenarios in Simulator

**Framework**: Xcode

Test hardware device-specific scenarios, such as Face ID or Touch ID authentication, fall detection, getting a memory warning, or location changes.

#### Overview

Some features that you support in your app can be challenging to test thoroughly on a hardware device. For example:

- Face ID and Touch ID each require a setup process. To test how your app handles the case when Face ID or Touch ID isn’t set up on a device, you would have to remove fingerprints or faces from your device, and then set them up again after that test.
- Fall detection requires significant setup and preparation to do repeated tests safely.
- To trigger a memory warning in your app on a device, you need to open up a number of other apps that consume memory, and coordinate it in such a way that your app receives the memory warning.
- iCloud syncing on a device may not happen as frequently as you need during your testing.
- Testing how your app responds to different locations or how it responds as you traverse a route can be time-consuming and difficult, especially in areas with poor cellular service.

Test these and other scenarios with Simulator’s hardware device feature support.

##### Test Face Id or Touch Id Authentication

Since Face ID and Touch ID each require a setup process, you need to test both how your app handles authentication when the user hasn’t configured Face ID or Touch ID yet, and when the user has configured them. To test the preconfigured state, choose Features > Face ID or Features > Touch ID, and deselect the Enrolled option. Select the Enrolled option to test the configured state.

When your app requests authentication, try a matching ID with Features > Face ID > Matching Face or Features > Touch ID > Matching Touch, or a non-matching ID with Features > Face ID > Non-matching Face or Features > Touch ID > Non-matching Touch.

##### Test a Simulated Fall

To test how your app responds to a detected fall in Simulator, choose Features > Simulate Fall, then choose one of the following fall response options to simulate:

- Confirmed
- Dismissed
- Rejected
- Unresponsive

##### Test a Memory Warning

Navigate to a place in your app where you’ve added code that responds to a memory warning, then choose Debug > Simulate Memory Warning. Confirm that your app responds appropriately.

##### Test Icloud Sync

Use Simulator to test data synchronization between iCloud and the simulated device. Use hardware devices for performance testing.

Create and use a separate Apple Account specifically for testing iCloud in Simulator. Sign in to iCloud on the simulated device.

Then, prepare your app as needed, and choose Features > Trigger iCloud Sync to trigger the system to synchronize updates with the server.

> **Note**: You must trigger synchronization manually because Simulator doesn’t support  notifications that trigger automatic data synchronization.

##### Test Changing Locations

Test how your app handles moving to a specific location, or moving along a route in Simulator.

Simulator contains some preset locations and routes. Choose Features > Location, and then select one of these options:

To set the location to a specific latitude and longitude:

1. Choose Features > Location > Custom Location…
2. Enter your location’s latitude and longitude in the dialog box.
3. Click OK to set the location.

To clear the location so that the simulated device has no location, choose Features > Location > None.

##### View the System Log

Use the system log to find errors, warnings, and other issues with your application. Choose Debug > Open System Log to open the system log for the simulated device in the Console app.

## See Also

- [Testing in Simulator versus testing on hardware devices](testing-in-simulator-versus-testing-on-hardware-devices.md)
  Review the differences between Simulator and hardware devices to determine which you should choose to test a scenario.
- [Sharing data with Simulator](sharing-data-with-simulator.md)
  Enter text directly in Simulator, or share location data, images, web addresses, files, or data from the clipboard with Simulator.
- [Identifying graphics and animations issues in Simulator](identifying-graphics-and-animations-issues-in-simulator.md)
  Reveal performance and display issues in your views with color overlays, and slow down animations to debug and improve them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/testing-complex-hardware-device-scenarios-in-simulator)*