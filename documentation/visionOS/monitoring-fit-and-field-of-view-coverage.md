# Monitoring fit and field of view coverage

**Framework**: visionOS

Respond to changes in fit and field of view coverage on Apple Vision Pro by using the Visual Fidelity API.

**Availability**:
- visionOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Some enterprise apps on Apple Vision Pro have a higher bar for fit accuracy and field of view coverage.

To maintain that level of accuracy and precision, use the Visual Fidelity API in ARKit to report how well the device fits the wearer and whether they see the required field of view. When fit accuracy or field of view coverage drifts out of range, the app can respond by coaching the wearer to adjust the fit or by making features that require accurate fit and field of view coverage unavailable.

The sample shows how to monitor visual fidelity and visualize the required field of view for use in your own app:

- In a shared space, the person configures monitoring, and the app displays live updates on fit accuracy and field of view coverage.
- In an immersive space, the app outlines the required field of view as a series of spheres along each eye’s boundary.

> **Note**: This sample requires an Apple Vision Pro. The Visual Fidelity API isn’t supported in the visionOS simulator.

#### Configure the Sample Code Project

Replace `Enterprise.license` with your license file. The sample app requires a valid license file to monitor visual fidelity.

#### Request the Entitlement

Visual fidelity monitoring is part of enterprise APIs for visionOS, a collection of APIs that unlock capabilities for enterprise customers. To use the Visual Fidelity API, you need to apply for the [`Visual Fidelity monitoring`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.arkit.visual-fidelity.allow) entitlement. For more information, including how to apply for this entitlement, see [`Building spatial experiences for business apps with enterprise APIs for visionOS`](building-spatial-experiences-for-business-apps-with-enterprise-apis.md).

#### Start Monitoring Visual Fidelity

When you launch the sample, `ContentView` displays a Start Monitoring button, a Show Visualization button, and three controls bound to properties on `AppModel`:

- **Field of View**: A picker for `FieldOfViewSelection` with six options. The four [`VisualFidelityProvider.FieldOfView`](https://developer.apple.com/documentation/ARKit/VisualFidelityProvider/FieldOfView) presets (A, B, C, and D) cover standard regions. A custom polygon defined by 2D points in tangent-angle coordinates gives precise geometric control. Device Fit Only skips field of view monitoring when the app doesn’t need to specify a required field of view.
- **Device Fit Updates**: A toggle for `requestDeviceFitUpdates`. Turn it on when the app needs to react to fit status, usually to coach the wearer to adjust the fit of their Vision Pro or to turn off features that depend on a valid fit. Each [`VisualFidelityData`](https://developer.apple.com/documentation/ARKit/VisualFidelityData) includes the wearer’s current [`deviceFitStatus`](https://developer.apple.com/documentation/ARKit/VisualFidelityData/deviceFitStatus). Turn it off when the app doesn’t need fit information. Then [`deviceFitStatus`](https://developer.apple.com/documentation/ARKit/VisualFidelityData/deviceFitStatus) always reports `.valid`.
- **Coaching Alerts**: A toggle for `presentCoachingAlerts`. Turn it on to let the system handle coaching. The system shows its own notices when fit or coverage drifts out of range. For example, a notice titled “Adjust Fit” with guidance like, “Move Vision Pro slightly up”. The system dismisses the notice automatically when the condition resolves. Turn it off when the app presents its own coaching UI.

When the wearer taps Start Monitoring, `ToggleMonitoringButton` calls `AppModel.startMonitoring()`. The `AppModel` captures the current selections, creates a [`VisualFidelityProvider`](https://developer.apple.com/documentation/ARKit/VisualFidelityProvider) with them, and runs it on an [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession):

```swift
// AppModel.swift

let session = ARKitSession()
let provider = VisualFidelityProvider(
    fieldOfView: fieldOfView,
    requestDeviceFitUpdates: requestDeviceFitUpdates,
    presentCoachingAlerts: presentCoachingAlerts
)

try await session.run([provider])
```

With the session running, ARKit delivers a stream of fidelity data to `AppModel`.

#### Respond to Fidelity Updates

When `AppModel` runs `monitor()`, it watches fidelity updates and stores the count, fit status, and field of view status that `StatusView` displays:

```swift
// AppModel.swift

group.addTask { [weak self, provider] in
    for await data in provider.fidelityDataUpdates {
        await self?.apply(data)
    }
}

@MainActor
private func apply(_ data: VisualFidelityData) {
    updateCount += 1
    deviceFitStatus = data.deviceFitStatus
    isFieldOfViewValid = data.isFieldOfViewValid
}
```

#### Visualize the Field of View

When the wearer taps the Show Visualization button, the app opens an immersive space where `ImmersiveView` outlines each eye’s field of view using a series of spheres, blue for the left eye, red for the right. The button isn’t available when the wearer selects a custom polygon or device fit only, since ARKit only delivers [`FieldOfViewAnchor`](https://developer.apple.com/documentation/ARKit/FieldOfViewAnchor) updates for presets.

When `AppModel` runs `monitor()`, it watches anchor updates and stores each one in `currentFieldOfViewAnchor`:

```swift
// AppModel.swift

group.addTask { [weak self, provider] in
    for await update in provider.anchorUpdates {
        await self?.setAnchor(update.anchor)
    }
}

@MainActor
private func setAnchor(_ anchor: FieldOfViewAnchor) {
    currentFieldOfViewAnchor = anchor
}
```

When `currentFieldOfViewAnchor` changes, `ImmersiveView` positions a pool of sphere entities to match the anchor’s per-eye polygon points:

```swift
// ImmersiveView.swift

.onChange(of: appModel.currentFieldOfViewAnchor, initial: true) { _, anchor in
    guard let anchor else {
        leftContainer.children.removeAll()
        rightContainer.children.removeAll()
        return
    }

    let anchorSpace = anchor.coordinateSpace(correction: .rendered)
    guard let transform = try? root.transform(from: anchorSpace) else { return }

    sync(leftContainer, to: anchor.leftPolygonPoints, transform: transform, material: Self.leftEyeMaterial)
    sync(rightContainer, to: anchor.rightPolygonPoints, transform: transform, material: Self.rightEyeMaterial)
}
```

Use the visualization to compare presets and confirm which one covers the regions your app depends on.

## See Also

- [Accessing the main camera](accessing-the-main-camera.md)
  Add camera-based features to enterprise apps.
- [Building spatial experiences for business apps with enterprise APIs for visionOS](building-spatial-experiences-for-business-apps-with-enterprise-apis.md)
  Grant enhanced sensor access and increased platform control to your visionOS app by using entitlements.
- [Locating and decoding barcodes in 3D space](locating-and-decoding-barcodes-in-3d-space.md)
  Create engaging, hands-free experiences based on barcodes in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/monitoring-fit-and-field-of-view-coverage)*