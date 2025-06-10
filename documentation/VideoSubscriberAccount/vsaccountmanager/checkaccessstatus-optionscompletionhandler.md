# checkAccessStatus(options:completionHandler:)

**Framework**: Video Subscriber Account  
**Kind**: method

Checks your app’s access to user subscription information, and requests access if needed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func checkAccessStatus(options: [VSCheckAccessOption : Any] = [:]) async throws -> VSAccountAccessStatus
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func checkAccessStatus(options: [VSCheckAccessOption : Any] = [:]) async throws -> VSAccountAccessStatus
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `options`: The options you use to check access status. For a list of possible options, see  .
- `completionHandler`: The closure the account manager executes after it checks your app’s access status. This closure has no return value and takes the following parameters:

## See Also

- [struct VSCheckAccessOption](vscheckaccessoption.md)
  The options your app uses when checking access status.
- [enum VSAccountAccessStatus](vsaccountaccessstatus.md)
  Constants that represent your app’s access status to the user’s subscription information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanager/checkaccessstatus(options:completionhandler:))*