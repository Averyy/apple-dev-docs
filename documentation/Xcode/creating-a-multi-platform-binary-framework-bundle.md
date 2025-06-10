# Creating a multiplatform binary framework bundle

**Framework**: Xcode

Combine variants of a binary framework or library into an XCFramework bundle that supports multiple platforms.

#### Overview

An XCFramework bundle, or , is a binary package created by Xcode that includes the frameworks and libraries necessary to build for multiple platforms (iOS, iPadOS, macOS, tvOS, visionOS, watchOS, and DriverKit), including Simulator builds. The frameworks can be static or dynamic and also include headers.

Include an XCFramework bundle inside a Swift package to distribute code in binary form for use in other projects. For more information, see [`Distributing binary frameworks as Swift packages`](distributing-binary-frameworks-as-swift-packages.md).

> **Note**: Session 417: [`Binary Frameworks in Swift`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/416)

##### Set Up the Project

To set up your project for creating an XCFramework, ensure your Xcode project has a scheme that builds only the framework target and its dependencies.

Configure these build settings on your target:

- Set the [`Build Libraries for Distribution`](build-settings-reference#Build-Libraries-for-Distribution.md) build setting to Yes. For Swift, this enables support for library evolution and generation of a module interface file.
- Set the [`Skip Install`](build-settings-reference#Skip-Install.md) build setting to No. If enabled, the built products aren‘t included in the archives.
- Leave the [`Architectures`](build-settings-reference#Architectures.md) build setting unset. The predefined value configures the target to build a universal binary for all the possible architectures the target platform uses.

For more information, see [`Customizing the build schemes for a project`](customizing-the-build-schemes-for-a-project.md) and [`Configuring the build settings of a target`](configuring-the-build-settings-of-a-target.md).

##### Create Archives for Frameworks or Libraries

Create an archive of your framework or library for each platform you wish to support by running `xcodebuild` in Terminal using the `archive` build action.

The following command archives a framework for the iOS platform:

```None
xcodebuild archive 
    -project MyFramework.xcodeproj
    -scheme MyFramework
    -destination "generic/platform=iOS"
    -archivePath "archives/MyFramework"
```

The system determines the architectures and SDK according to build settings when running the command with the `-destination` flag, like the example above. Avoid common errors by using this flag rather than `-arch` and `-sdk`.

To build an archive for a different platform, adjust the value for `-destination`. Replacing this value with `"generic/platform=iOS Simulator"` creates an archive for Simulator.

An XCFramework can contain versions of your framework built for macOS with and without Mac Catalyst. To generate an archive for the Mac Catalyst variant, use `"generic/platform=macOS,variant=Mac Catalyst"`, adding the the variant type to the `-destination` value.

To see an extensive list of all the command options, execute `xcodebuild` with the `-help` flag.

> **Note**: Clients of your XCFramework need it to support all the possible architectures the platform uses. As platforms move forward to adopt new architectures, such as the adoption of Apple silicon by macOS and iOS Simulator, keep the binaries your XCFramework includes up to date by rebuilding the frameworks and libraries to include new architectures. To determine the architectures of a binary, see [`Determine the architectures a binary supports`](creating-a-multi-platform-binary-framework-bundle#Determine-the-architectures-a-binary-supports.md).

##### Generate the Xcframework Bundle

To package the built content of a given framework or library for multiple platforms and variants into a single XCFramework bundle, execute `xcodebuild` with the `-create-xcframework` option.

The following command creates an XCFramework with variants for iOS, iOS Simulator, macOS, and Mac Catalyst:

```None
xcodebuild -create-xcframework
    -archive archives/MyFramework-iOS.xcarchive -framework MyFramework.framework
    -archive archives/MyFramework-iOS_Simulator.xcarchive -framework MyFramework.framework
    -archive archives/MyFramework-macOS.xcarchive -framework MyFramework.framework
    -archive archives/MyFramework-Mac_Catalyst.xcarchive -framework MyFramework.framework
    -output xcframeworks/MyFramework.xcframework
```

To include a static library file (`.a` file), replace `-framework` with `-library` in the command above.

If the content you wish to include exists outside of an archive, provide paths for the instances of `-framework` or `-library` and include paths to headers using the additional `-headers` flag.

```None
xcodebuild -create-xcframework
    -library products/iOS/usr/local/lib/libMyLibrary.a -headers products/iOS/usr/local/include
    -library products/iOS_Simulator/usr/local/lib/libMyLibrary.a -headers products/iOS/usr/local/include
    -library products/macOS/usr/local/lib/libMyLibrary.a -headers products/macOS/usr/local/include
    -library products/Mac\ Catalyst/usr/local/lib/libMyLibrary.a -headers products/Mac\ Catalyst/usr/local/include
    -output xcframeworks/MyLibrary.xcframework
```

To see all the options the XCFramework utility supports, execute:

```None
xcodebuild -create-xcframework -help
```

##### Sign the Xcframework Bundle

Signing your XCFramework using your code signing identity informs developers who use your framework that it came from you and that it hasn’t been tampered with since you added the signature. To sign your framework, run the following command:

```None
% codesign --timestamp -s <identity> xcframeworks/MyLibrary.xcframework
```

To sign a framework for distribution as a member of the Apple Developer Program, your code signing identity should be an Apple Distribution or Apple Development identity. To sign a framework for distribution as a member of an Enterprise Program, use an iOS Distribution or iOS App Development identity. You don’t need to supply the full name of your code signing identity after the `-s` option. Use a string that uniquely identifies the code signing identity in the keychain you use to sign the XCFramework. For more information on the `codesign` tool, see the UNIX manual page for `codesign`.

> ❗ **Important**:  If you revoke a certificate for a code signing identity that you use to sign frameworks for distribution, sign the framework with a different code signing identity that isn’t revoked and share that version with developers who use your framework. The Xcode build system fails with an error when it encounters a framework with a code signature that contains a revoked certificate.

##### Avoid Issues When Using Alternate Build Systems

When using an alternative build system, common for open source projects, follow a similar process to compile the source code into static library files, using one binary per platform, or . Use the files to create the XCFramework.

- For each library and each platform, build a binary static libary file (`.a` file) that includes slices for all the possible architectures the platform uses.
- Specify the path to each of the binaries you create in a call to `xcodebuild -create-xcframework` to generate the XCFramework.

Avoid wrapping a static library in a `.framework` bundle and omitting the `.a` extension. Use the `-library` flag to create an XCFramework with a static library; see the example above under [`Generate the XCFramework bundle`](creating-a-multi-platform-binary-framework-bundle#Generate-the-XCFramework-bundle.md).

Avoid using tools such as `lipo` to combine architecture slices built for iOS and iOS Simulator into a single binary. The static library files for iOS and iOS Simulator must remain seperate. For an XCFramework that supports iOS and iOS Simulator, you produce at least two binary static library files. The binary iOS devices use is built for ARM64. The universal binary for Simulator includes slices for x86_64 and ARM64 for Apple silicon.

Avoid using dynamic library files (`.dylib` files) for dynamic linking. An XCFramework can include dynamic library files, but only macOS supports these libraries for dynamic linking. Dynamic linking on iOS, iPadOS, tvOS, visionOS, and watchOS requires the XCFramework to contain `.framework` bundles.

If you have further questions on how to compile the library to meet these goals, work with support for the library vendor.

##### Determine the Architectures a Binary Supports

Projects that link to your XCFramework require that it contains universal binaries covering the architectures each platform builds for.

To determine the architectures an existing binary includes, execute `file` from Terminal and provide the path to the binary.

```None
file <PathToFramework>/<FrameworkName>.framework/<FrameworkName>
```

```None
file <PathToLibrary>/libMyLibrary.a
```

## See Also

- [Creating a static framework](creating-a-static-framework.md)
  Configure your project to build a new static framework.
- [Identifying and addressing framework module issues](identifying-and-addressing-framework-module-issues.md)
  Detect and fix common problems found in framework modules with the module verifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-a-multi-platform-binary-framework-bundle)*