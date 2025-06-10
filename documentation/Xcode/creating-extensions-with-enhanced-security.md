# Creating extensions with enhanced security

**Framework**: Xcode

Reduce opportunities for an attacker to target your app through its extensions.

#### Overview

Separating sensitive calculations, such as handling data from untrusted sources, into extensions that the system runs as separate processes from your app reduces the opportunity for attackers to target the sensitive calculation and gain access to other parts of your app or the system. Create enhanced security extensions on iOS, iPadOS, and macOS to enforce tighter sandbox restrictions, and enable compiler and runtime security protections.

##### Define the Extension Point in Your App

Add the `EX_ENABLE_EXTENSION_POINT_GENERATION` user-defined build setting with the value `YES` to your app target’s build setting. In your app’s source code, create an extension to [`AppExtensionPoint`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint) that defines your app’s extension point. Give the extension point the [`AppExtensionPoint.Name`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/Name) of your choosing, and the [`AppExtensionPoint.EnhancedSecurity`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/EnhancedSecurity) attribute to tell the system to run your extension in the enhanced security runtime:

```swift
import ExtensionFoundation

extension AppExtensionPoint {
  @Definition
  static var exampleExtension: AppExtensionPoint {
    Name("exampleExtension")
    EnhancedSecurity()
  }
}
```

##### Create the Extension

Follow these steps to create the extension:

1. In Xcode, choose File > New > Target, and select the Generic Extension template.
2. Select the Enhanced Security Extension extension type, and click Finish.
3. In the Xcode project navigator, delete the extension target’s `Info.plist` file.
4. In the target build settings editor, delete the `INFOPLIST_FILE` build setting for the extension target.

Edit the main source file for the extension, so that the [`AppExtensionPoint.Identifier`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/Identifier) for the extension point it binds to has your app’s bundle ID as the host identifier, and the name you gave the extension point in the previous section:

```swift
import ExtensionFoundation

@main
struct MyAppHelper: ExampleExtension {
  @AppExtensionPoint.Bind
  var boundExtensionPoint: AppExtensionPoint {
    AppExtensionPoint.Identifier(host: "com.example.my-app", name: "exampleExtension")
  }
}
```

Write the code to implement your extension’s behavior. The system runs your extension in a sandbox that restricts access to most system services and frameworks. In particular, your extension can’t present UI. Instead, it must communicate with its host app, and ask the app to present UI and interact with other system services on the extension’s behalf.

##### Discover and Launch the Extension

In your app, create an [`AppExtensionPoint.Monitor`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/Monitor) to discover the enhanced security extension:

```swift
let monitor = try await AppExtensionPoint.Monitor(appExtensionPoint: AppExtensionPoint.exampleExtension)
guard let identity = monitor.identities.first else {     
   fatalError("Extension not found")
} 
```

The `identity` represents the bundle for the enhanced security extension you created in the previous section. Create an [`AppExtensionProcess`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionProcess) with that bundle to launch the extension:

```swift
do {
  self.process = try await AppExtensionProcess(configuration: .init(appExtensionIdentity: identity, onInterruption: {
    // The system calls this closure when the extension exits.
  }))
  // Communicate with the extension.
}
catch let error {
  // The system can't launch the extension.
}
```

##### Communicate Between the App and the Extension

Use [`XPCSession`](https://developer.apple.com/documentation/XPC/XPCSession) to handle communication between your app and its enhanced security extension. For more information, see [`Creating XPC services`](https://developer.apple.com/documentation/XPC/creating-xpc-services).

Define structures that conform to [`Codable`](https://developer.apple.com/documentation/Swift/Codable) in code you share between the app and extension, and create instances of those structures to send over XPC using the session you create:

```swift
struct Message: Identifiable, Codable {
  var id: String
  // Add properties that represent data your app sends to its extension.

  struct Response: Codable {
    // Define another structure that the extension sends back to the app in its reply.
  }
}
```

Call [`makeXPCSession()`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionProcess/makeXPCSession()) in your app to create an `XPCSession` you use to send messages to the extension:

```swift
do {
  self.xpcSession = try process.makeXPCSession()
  try xpcSession.activate()
  // Send messages to the extension.
}
catch let error {
  // The system can't create the XPC session.
}
```

Use the session you create to send messages to the extension, and receive responses:

```swift
let response = try await withCheckedThrowingContinuation { continuation in
  do {
    // Construct the message the app sends to the extension.
    let message = Message()
    try xpcSession.send(Message()) { result in
      switch result {
      case .success(let reply):
        let response = (try? reply.decode(as: Message.Response.self)) ?? /* Create a default response. */
        continuation.resume(returning: response)
      case .failure(let error):
        continuation.resume(throwing: error)
      }
    }
  }
  catch {
    continuation.resume(throwing: error)
  }
}
// Interpret the response from the extension.
```

In the extension, create a [`ConnectionHandler`](https://developer.apple.com/documentation/ExtensionFoundation/ConnectionHandler) to accept incoming connections from the app. Call the [`init(onSessionRequest:)`](https://developer.apple.com/documentation/ExtensionFoundation/ConnectionHandler/init(onSessionRequest:)) initializer, and use the closure to accept the XPC connection and create a session.

```swift
extension ExampleExtension {
    var configuration: some AppExtensionConfiguration {
        // Return your extension's configuration upon request.
        return ConnectionHandler(onSessionRequest: { request in
            let handler = MessageHandler(appExtension: self)
            return request.accept { session in
                return handler
            }
        })
    }
}
 
fileprivate struct MessageHandler<E: ExampleExtension>: XPCPeerHandler, Sendable {
    let appExtension: E
     
    func handleIncomingRequest(_ message: Message) -> (any Encodable)? {
        // Process the incoming message.
        return Message.Response()
    }
}

```

##### Adopt Other Security Hardening Features

Enhanced security extensions use the same compiler and runtime security features as apps that adopt the Enhanced Security capability. For more information, see [`Enabling enhanced security for your app`](enabling-enhanced-security-for-your-app.md).

## See Also

- [Verifying the origin of your XCFrameworks](verifying-the-origin-of-your-xcframeworks.md)
  Discover who signed a framework, and take action when that changes.
- [Enabling enhanced security for your app](enabling-enhanced-security-for-your-app.md)
  Detect out-of-bounds memory access, use of freed memory, and other potential vulnerabilities.
- [Adopting type-aware memory allocation](adopting-type-aware-memory-allocation.md)
  Reduce the opportunities to treat pointers as data in your code.
- [Conforming to Mach IPC security restrictions](conforming-to-mach-ipc-security-restrictions.md)
  Avoid crashes and potentially insecure situations associated with Mach messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-extensions-with-enhanced-security)*