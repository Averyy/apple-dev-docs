# Updating your app from 32-bit to 64-bit architecture

**Framework**: UIKit

Ensure that your app behaves as expected by adapting it to support later versions of the operating system.

#### Overview

In iOS 11 and later, all apps use the 64-bit architecture. If your app targets an earlier version of iOS, you must update it to run on later versions.

##### Update Your App to the Latest Sdk

Begin by updating your existing app to iOS 11 or later. By updating your app first, you can remove deprecated code paths, address any compiler warnings, and search your code for specific 64-bit issues.

1. Install the latest version of Xcode and open your project. Xcode prompts you to  the project. Modernizing adds new warnings and errors that are important when compiling your app for 64-bit architecture.
2. Update your project settings to support the latest version of iOS. You can’t build a 64-bit project if it targets an iOS version earlier than iOS 5.1.
3. Change the Architectures build setting in your project to Standard Architectures.
4. Update your app to support the 64-bit runtime environment. The new compiler warnings and errors help guide you through this process.
5. Test your app on actual 64-bit hardware. Don’t rely on the Simulator app. Although it can be helpful during development, some changes, such as the function-calling conventions, are visible only when your app is running on a device.
6. Tune your app’s memory performance by using Instruments.

##### Audit Your Code

It’s critical that you review your code for proper pointer usage. Assumptions in pointer sizes can lead to erratic behavior and even crashes. Focus on the following areas:

- [`Updating data structures`](updating-data-structures.md). Eliminate assumptions about type size and alignment in structures, and use explicit data types.
- [`Auditing pointer usage`](auditing-pointer-usage.md). Adhere to proper casting behaviors and review your methods for allocating memory.
- [`Managing functions and function pointers`](managing-functions-and-function-pointers.md) Use function prototypes for safety, and review the calling of functions that have variable-length argument lists.

With pointer usage addressed, your app should be stable and you can focus on performance and optimize accordingly:

- [`Optimizing memory performance`](optimizing-memory-performance.md). Establish performance tests that measure your use of memory in the context of 64-bit runtime.
- [`Verifying mathematical calculations`](verifying-mathematical-calculations.md). Verify signed values in math operations to ensure accurate results, and review your use of bit mask operations.

## Topics

### Memory and pointer access
- [Updating data structures](updating-data-structures.md)
  Review your app’s data design and update it to conform with 64-bit architecture.
- [Auditing pointer usage](auditing-pointer-usage.md)
  Ensure that the pointers in your code are safe for the 64-bit runtime.
- [Managing functions and function pointers](managing-functions-and-function-pointers.md)
  Ensure that your code correctly handles functions, function pointers, and Objective-C messages.
### Performance and accuracy
- [Optimizing memory performance](optimizing-memory-performance.md)
  Measure the impact of the 64-bit runtime on your app’s memory usage.
- [Verifying mathematical calculations](verifying-mathematical-calculations.md)
  Ensure the accuracy of your math operations in 64-bit architecture.

## See Also

- [func UIApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?, String?) -> Int32](uiapplicationmain(_:_:_:_:)-1yub7.md)
  Creates the application object and the application delegate and sets up the event cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/updating-your-app-from-32-bit-to-64-bit-architecture)*