# Drawing in the air and on surfaces with a spatial stylus

**Framework**: visionOS

Create a spatial stylus drawing experience that balances latency and accuracy for both in-air and on-surface drawing.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

This sample demonstrates how to build an interactive drawing app that responds to spatial stylus input in visionOS. It shows how to track a spatial stylus in 3D space, synchronize stylus button inputs with tracking information, and balance latency with accuracy by predicting brush strokes and correcting them over time. The sample also addresses the unique challenges of on-surface drawing.

The key techniques the sample demonstrates are as follows:

- : Reduce the lag a person experiences when drawing by predicting anchors for the initial stroke rendering and correcting with the latest anchors for accuracy over time.
- : Adjust prediction strategies based on drawing context—using shorter prediction horizons or latest anchors directly when drawing on surfaces to minimize jitter, and longer prediction horirzons when drawing in air.
- : Reduce swimming artifacts between virtual brush strokes and the real world when drawing on physical surfaces by transitioning strokes from the [`ARKitCoordinateSpace.Correction.rendered`](https://developer.apple.com/documentation/ARKit/ARKitCoordinateSpace/Correction/rendered) coordinate space to the [`ARKitCoordinateSpace.Correction.none`](https://developer.apple.com/documentation/ARKit/ARKitCoordinateSpace/Correction/none) coordinate space.

> **Note**: This sample uses the low-level mesh drawing implementation from [`Creating a spatial drawing app with RealityKit`](https://developer.apple.com/documentation/RealityKit/creating-a-spatial-drawing-app-with-realitykit) as its foundation.

#### Discover and Track the Active Stylus

Before any drawing can happen, the app must first discover available styli, establish a connection with one, and begin tracking its movements in 3D space.

The `StylusModel` class in the sample manages stylus connections and tracking, starting with the `handleStylusConnections` method which it calls on initialization:

```swift
class StylusModel {
    /// The spatial stylus the app is actively tracking.
    private(set) var activeStylus: GCStylus? = nil
    /// The tracking provider which provides tracking information about the spatial stylus.
    private var accessoryTrackingProvider: AccessoryTrackingProvider? = nil
    /// The ARKit session which runs the accessory tracking provider.
    private let arKitSession = ARKitSession()

    // ...

    init() {
        // ...
        Task {
            await handleStylusConnections()
        }
    }

    // ...

    /// Updates the active stylus when a stylus connects or disconnects.
    private func handleStylusConnections() async {
        // Set the first spatial styli the app already has a connection with as active, if there is one.
        if let stylus = GCStylus.styli.first(where: { $0.productCategory == GCProductCategorySpatialStylus }) {
            await setActiveStylus(stylus: stylus)
        }
        
        // Listen for stylus connection notifications to set the active stylus when one connects.
        NotificationCenter.default.addObserver(forName: NSNotification.Name.GCStylusDidConnect, object: nil, queue: nil) { notification in
            if let stylus = notification.object as? GCStylus, stylus.productCategory == GCProductCategorySpatialStylus {
                Task { @MainActor in
                    await self.setActiveStylus(stylus: stylus)
                }
            }
        }
        
        // Remove the active stylus when the app receives a stylus disconnection notification.
        NotificationCenter.default.addObserver(forName: NSNotification.Name.GCStylusDidDisconnect, object: nil, queue: nil) { notification in
            if let stylus = notification.object as? GCStylus, stylus.productCategory == GCProductCategorySpatialStylus {
                Task { @MainActor in
                    if stylus == self.activeStylus {
                        withAnimation {
                            self.activeStylus = nil
                        }
                        self.arKitSession.stop()
                    }
                }
            }
        }
    }
}
```

The `setActiveStylus` method updates the `activeStylus` property and runs accessory tracking for the stylus:

```swift
private func setActiveStylus(stylus: GCStylus) async {
    guard stylus != activeStylus else {
        return
    }
    
    // Set the active stylus.
    withAnimation {
        activeStylus = stylus
    }
    
    // Update the input state queue depth to buffer inputs.
    activeStylus?.input?.inputStateQueueDepth = 100
    
    // Create the accessory tracking provider.
    await runAccessoryTracking(for: stylus)
}
```

The sample wraps updates to the value of `activeStylus` in [`withAnimation(_:_:)`](https://developer.apple.com/documentation/SwiftUI/withAnimation(_:_:)) blocks so that SwiftUI views can animate their content when its value changes. For example, the `StylusSettingsHeaderView` animates a symbol displaying whether the person has connected a stylus by observing this value:

```swift
struct StylusSettingsHeaderView: View {
    // ...
    
    var body: some View {
        // ...
        let isStylusActive = stylusModel.activeStylus != nil
        Image(systemName: isStylusActive ? "pencil" : "pencil.slash")
            .contentTransition(.symbolEffect(.replace))
            .help(isStylusActive ? "Stylus: Connected" : "Stylus: Not Connected")
        // ...
    }
}
```

Finally, the `runAccessoryTracking` method initializes the [`AccessoryTrackingProvider`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider) with the stylus and runs the [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession):

```swift
private func runAccessoryTracking(for stylus: GCStylus) async {
    guard let accessory = try? await Accessory(device: stylus) else {
        return
    }
    
    // Create the accessory tracking provider.
    accessoryTrackingProvider = AccessoryTrackingProvider(accessories: [accessory])
    if let accessoryTrackingProvider {
        try? await arKitSession.run([accessoryTrackingProvider])
    }
}
```

For more information about discovering and tracking spatial styli, see [`Discovering and tracking spatial game controllers and styli`](https://developer.apple.com/documentation/GameController/discovering-and-tracking-spatial-game-controllers-and-styli).

#### Capture Stylus Button Inputs

The sample captures input data from each of the active stylus’ buttons every frame.

The `StylusButtonInput` structure encapsulates relevant information about button input, including its source, whether it’s pressed, its pressure, and its timestamp:

```swift
struct StylusButtonInput {
    enum Source {
        case none
        case tip
        case primary
        case secondary
    }
    
    var source: Source
    var isPressed: Bool
    var pressure: Float
    var timestamp: TimeInterval
}
```

The `getLatestStylusButtonInputs` method in `StylusModel` populates an array of `StylusButtonInput` structures by retrieving all available inputs from the active stylus’ input queue:

```swift
func getLatestStylusButtonInputs() -> [StylusButtonInput] {
    guard let stylusInput = activeStylus?.input else {
        return []
    }
    
    var inputs: [StylusButtonInput] = []
    // Iterate over each input state in the queue.
    while let nextInputState = stylusInput.nextInputState() {
        // Get the pressed input for the tip and secondary buttons.
        guard let stylusTipInput = nextInputState.buttons[.stylusTip]?.pressedInput,
              let stylusPrimaryInput = nextInputState.buttons[.stylusPrimaryButton]?.pressedInput,
              let stylusSecondaryInput = nextInputState.buttons[.stylusSecondaryButton]?.pressedInput else {
            continue
        }
        
        let inputsBySource = [StylusButtonInput.Source.tip: stylusTipInput,
                              StylusButtonInput.Source.primary: stylusPrimaryInput,
                              StylusButtonInput.Source.secondary: stylusSecondaryInput]
        
        // Set the input's `isPressed` state to true if the person is pressing any of the buttons.
        let isPressed = inputsBySource.values.contains(where: { $0.isPressed })
        // Set the pressure as the maximum value amongst all the input buttons.
        let maximumPressureInput = inputsBySource.max(by: { $0.value.value < $1.value.value })!
        let pressure = maximumPressureInput.value.value
        // Set the source of the input as the button with the greatest pressure, or none if the pressure is zero.
        let source = pressure > 0 ? maximumPressureInput.key : .none
        
        // Create and append the input.
        let input = StylusButtonInput(source: source, isPressed: isPressed, pressure: pressure, timestamp: nextInputState.lastEventTimestamp)
        inputs.append(input)
    }
    
    return inputs
}
```

> **Note**: While button press notification do exist (see [`Handling input events`](https://developer.apple.com/documentation/GameController/handling-input-events#Receive-callbacks-for-input-changes)), in this case the app requires the lowest latency possible for button presses to synchronize them with accessory anchors. As the update loop already notifies the app on every frame render the app can efficiently query the button state at that point.

It’s also important to increase the input queue depth to be large enough to buffer all of the inputs the app could receive from the stylus in a single frame, otherwise the app can miss inputs:

```swift
activeStylus?.input?.inputStateQueueDepth = 100
```

The `DrawingInputProvider` class calls `getLatestStylusButtonInputs` each frame and maintains a history of button state changes. This is crucial for determining exactly when to start and stop drawing strokes, creating a more precise drawing experience:

```swift
class DrawingInputProvider {
    // ...

    /// A buffer of all of the most recent stylus button inputs.
    private var allButtonInputs: [StylusButtonInput] = []
    /// A buffer of each stylus button input whose `isPressed` value is different from the prior button input.
    private var changedButtonInputs: [StylusButtonInput] = []

    // ...

    /// Updates button input buffers with the latest stylus button inputs.
    private func updateButtonInputs() {
        // Append the latest button inputs.
        let latestStylusButtonInputs = stylusModel.getLatestStylusButtonInputs()
        allButtonInputs.append(contentsOf: latestStylusButtonInputs)

        // Append new changed button inputs.
        for stylusButtonInput in latestStylusButtonInputs {
            // Override the `isPressed` property of the input when the brush state is in calligraphic mode.
            // In calligraphic mode, the app considers the input pressed
            // if its pressure exceeds the lower bound of the pressure threshold for drawing.
            var stylusButtonInput = stylusButtonInput
            if case let .calligraphic(pressureRange, _) = appModel.brushState.settings.thicknessType {
                stylusButtonInput.isPressed = stylusButtonInput.pressure > pressureRange.lowerBound
            }
            // Append the input if its pressed state differs from the last changed input.
            if stylusButtonInput.isPressed != changedButtonInputs.last?.isPressed {
                changedButtonInputs.append(stylusButtonInput)
            }
        }
    }
}
```

This sample app supports two brush types, uniform and calligraphic. For the uniform type the sample creates strokes with a constant radius. For the calligraphic type, the radius of the strokes depends on the button input pressure. Here, the sample overrides the button input’s `isPressed` property when in calligraphic mode to allow the person to set a specific pressure threshold to start and stop drawing.

#### Get Stylus Anchor Inputs

The sample stores tracking information about the stylus’ position and timestamp in the `StylusAnchorInput` structure:

```swift
struct StylusAnchorInput {
    let position: SIMD3<Float>
    let timestamp: TimeInterval
}
```

The `getAnchorInput` method in `DrawingInputProvider` populates a `StylusAnchorInput` structure by obtaining an [`AccessoryAnchor`](https://developer.apple.com/documentation/ARKit/AccessoryAnchor) for the given tracking mode, and extracting its position relative to an entity with the given [`ARKitCoordinateSpace.Correction`](https://developer.apple.com/documentation/ARKit/ARKitCoordinateSpace/Correction):

```swift
private func getAnchorInput(trackingMode: TrackingMode, correction: ARKitCoordinateSpace.Correction, relativeTo: Entity) -> StylusAnchorInput? {
    guard let anchor = switch trackingMode {
        case .predicted(let predictionHorizon):
            stylusModel.getPredictedStylusAnchor(at: CACurrentMediaTime() + predictionHorizon)
        case .latest:
            stylusModel.getLatestStylusAnchor()
    }, let position = stylusModel.getStylusTipPosition(for: anchor, correction: correction, relativeTo: relativeTo) else {
        return nil
    }
    return StylusAnchorInput(position: position, timestamp: anchor.timestamp)
}
```

The `StylusModel` implements the `getLatestStylusAnchor`,  `getPredictedStylusAnchor`, and `getStylusTipPosition` methods as follows:

```swift
/// Gets the latest stylus anchor.
func getLatestStylusAnchor() -> AccessoryAnchor? {
    guard accessoryTrackingProvider?.state == .running else {
        return nil
    }
    return accessoryTrackingProvider?.latestAnchors.first
}

/// Predicts a new stylus anchor for a given timestamp.
func getPredictedStylusAnchor(at timestamp: TimeInterval) -> AccessoryAnchor? {
    guard let accessoryTrackingProvider,
          let latestStylusAnchor = getLatestStylusAnchor() else {
        return nil
    }
    return accessoryTrackingProvider.predictAnchor(for: latestStylusAnchor, at: timestamp)
}

/// Gets the tip position of the stylus relative to an entity for a given anchor and correction.
func getStylusTipPosition(for anchor: AccessoryAnchor, correction: ARKitCoordinateSpace.Correction, relativeTo: Entity) -> SIMD3<Float>? {
    guard let position = try? anchor.coordinateSpace(for: .aim, correction: correction).convert(value: Point3DFloat.zero, to: relativeTo) else {
        return nil
    }
    return [position.x, position.y, position.z]
}
```

#### Capture Initial and Final Anchor Inputs

The app takes a dual-input approach to drawing that provides immediate visual feedback while also applying corrections for greater accuracy. Specifically, the app captures both “initial” and “final” stylus anchor inputs every frame, and later corrects the initial anchors with the final anchors over time to achieve a balance between low-latency and high-accuracy brush strokes.

The `getCurrentStylusInputState` method in `DrawingInputProvider` gets the initial and final anchor inputs each frame:

```swift
/// A structure for storing state for the inital and final stylus anchor and button inputs.
struct StylusInputState {
    var initialAnchorInput: StylusAnchorInput
    var initialChangedButtonInputIndex: Int
    var finalAnchorInput: StylusAnchorInput
    var finalChangedButtonInputIndex: Int
}

// ...

/// Get the current input state for the stylus, including its anchor and button inputs.
private func getCurrentStylusInputState(relativeTo: Entity) -> StylusInputState? {
    // Get the current drawing medium.
    guard let drawingMedium = getCurrentDrawingMedium() else {
        return nil
    }
    
    // Get the drawing settings for the current drawing medium.
    let drawingSettings = switch drawingMedium {
        case .air:
            appModel.airDrawingSettings
        case .surface:
            appModel.surfaceDrawingSettings
    }
    // Get the initial and final anchor inputs and buttons given the drawing settings.
    guard let initialAnchorInput = getAnchorInput(trackingMode: drawingSettings.initialDrawingTracking,
                                                  correction: .rendered,  // Always use rendered correction for initial anchors.
                                                  relativeTo: relativeTo),
          let initialChangedButtonInputIndex = getChangedButtonInputIndex(for: initialAnchorInput),
          let finalAnchorInput = getAnchorInput(trackingMode: .latest,  // Always use latest tracking for final anchors.
                                                correction: drawingSettings.finalDrawingCorrection.arKitMode,
                                                relativeTo: relativeTo),
          let finalChangedButtonInputIndex = getChangedButtonInputIndex(for: finalAnchorInput) else {
        return nil
    }
    
    return StylusInputState(
        initialAnchorInput: initialAnchorInput,
        initialChangedButtonInputIndex: initialChangedButtonInputIndex,
        finalAnchorInput: finalAnchorInput,
        finalChangedButtonInputIndex: finalChangedButtonInputIndex
    )
}
```

To minimize latency, the sample uses predicted anchors for the initial stylus anchor inputs, and the latest anchors for the final inputs. Additionally, the sample uses the [`ARKitCoordinateSpace.Correction.rendered`](https://developer.apple.com/documentation/ARKit/ARKitCoordinateSpace/Correction/rendered) correction for initial inputs to ensure the stroke aligns with the tip of the pen, and [`ARKitCoordinateSpace.Correction.none`](https://developer.apple.com/documentation/ARKit/ARKitCoordinateSpace/Correction/none) for final anchors when drawing on a surface so that the virtual drawing aligns with the real world surface and straight lines remain straight:

```swift
var surfaceDrawingSettings = DrawingSettings(
    initialDrawingTracking: .predicted(predictionHorizon: 0),
    finalDrawingCorrection: .none
)
var airDrawingSettings = DrawingSettings(
    initialDrawingTracking: .predicted(predictionHorizon: 0.01),
    finalDrawingCorrection: .rendered
)
```

> **Note**: The app uses a shorter prediction horizon for drawing on surfaces to reduce jitter. You can also use the latest anchors directly instead of predicting to minimize jitter as much as possible when drawing on surfaces. In air, you can use a comparatively longer prediction horizon before jitter becomes an issue.

#### Synchronize Stylus Position with Button Inputs

Creating a fluid drawing experience requires precise synchronization between the stylus’s position in 3D space and its button input data. The `DrawingInputProvider` class is responsible for this synchronization. Each frame it queries for stylus anchors and aligns them with button inputs to create drawing inputs.

Drawing inputs include all the information a stylus anchor input provides, along with an additional field for the button pressure and a Boolean specifying whether the person is drawing for that input:

```swift
struct DrawingInput {
    let position: SIMD3<Float>
    let timestamp: TimeInterval
    let pressure: Float
    let isDrawing: Bool
    
    init(with stylusAnchorInput: StylusAnchorInput, pressure: Float, isDrawing: Bool) {
        self.position = stylusAnchorInput.position
        self.timestamp = stylusAnchorInput.timestamp
        self.pressure = pressure
        self.isDrawing = isDrawing
    }
}
```

Because the button inputs in the `allButtonInputs` and `changedButtonInputs` arrays are already in ascending order by timestamp, the `DrawingInputProvider` can query the button state at a given anchor timestamp and align anchors with button inputs; for example:

```swift
/// Gets whether the stylus button is pressed for a given anchor.
private func isButtonPressed(for anchorInput: StylusAnchorInput) -> Bool {
    changedButtonInputs.last(where: { anchorInput.timestamp >= $0.timestamp })?.isPressed == true
}

/// Gets the button pressure at an anchor's timestamp.
private func getButtonPressure(for anchorInput: StylusAnchorInput) -> Float {
    allButtonInputs.last(where: { anchorInput.timestamp >= $0.timestamp })?.pressure ?? 0
}
```

The `getDrawingInputs` method is responsible for converting stylus anchor inputs into drawing inputs. This method creates a `DrawingInput` from the current `StylusAnchorInput` by querying the button pressure and button pressed state for that input:

```swift
/// Gets the drawing inputs for an anchor input.
private func getDrawingInputs(previousChangedButtonInputIndex: Int,
                              previousInput: StylusAnchorInput,
                              currentInput: StylusAnchorInput) -> [DrawingInput] {
    var drawingInputs: [DrawingInput] = []
    
    // Append intermediate drawing inputs.
    drawingInputs
        .append(
            contentsOf: getIntermediateDrawingInputs(
                previousChangedButtonInputIndex: previousChangedButtonInputIndex,
                previousInput: previousInput,
                currentInput: currentInput
            )
        )
    
    // Append the current drawing input.
    let pressure = getButtonPressure(for: currentInput)
    let isDrawing = isButtonPressed(for: currentInput)
    drawingInputs.append(DrawingInput(with: currentInput, pressure: pressure, isDrawing: isDrawing))
    return drawingInputs
}
```

The `getDrawingInputs` method also adds any intermediate inputs that the person initiated between the current and previous anchor input with the `getIntermediateDrawingInputs` method. For example, the person may have quickly pressed and released a button between the previous and current anchor input, which the `DrawingInputProvider` would otherwise miss if it didn’t check the intermediary button inputs between the previous and current anchor input:

```swift
/// Gets any drawing inputs occurring between the previous and current anchor input.
private func getIntermediateDrawingInputs(previousChangedButtonInputIndex: Int,
                                          previousInput: StylusAnchorInput,
                                          currentInput: StylusAnchorInput) -> [DrawingInput] {
    var intermediateDrawingInputs: [DrawingInput] = []
    guard let currentChangedButtonInputIndex = getChangedButtonInputIndex(for: currentInput) else {
        return intermediateDrawingInputs
    }
    
    // Append additional drawing inputs for any button inputs occurring between the last and current drawing inputs.
    if previousChangedButtonInputIndex < currentChangedButtonInputIndex {
        for changedButtonInputIndex in (previousChangedButtonInputIndex + 1)...currentChangedButtonInputIndex {
            let buttonInput = changedButtonInputs[changedButtonInputIndex]
            let timestamp = buttonInput.timestamp
            
            let deltaTime = currentInput.timestamp - previousInput.timestamp
            let interpolationTime = deltaTime == 0 ? 1 : Float(simd_clamp(timestamp - previousInput.timestamp / deltaTime, 0, 1))
            
            let interpolatedInput = mix(previousInput, currentInput, interpolationTime)
            
            // When the person presses the button, stop the previous stroke before starting a new stroke,
            // and vice-versa when the person releases the button.
            let pressure = getButtonPressure(for: interpolatedInput)
            intermediateDrawingInputs.append(DrawingInput(with: interpolatedInput, pressure: pressure, isDrawing: !buttonInput.isPressed))
            intermediateDrawingInputs.append(DrawingInput(with: interpolatedInput, pressure: pressure, isDrawing: buttonInput.isPressed))
        }
    }
    return intermediateDrawingInputs
}
```

The `provideLatestInputs` method ties everything together; it:

- Updates the button inputs
- Retrieves the current stylus anchor input states for the initial and final drawing
- Generates drawing inputs from them to pass to the `DrawingDocument`

```swift
/// Provide the latest drawing inputs to a drawing document.
func provideLatestInputs(to drawingDocument: DrawingDocument) {
    // Update the button inputs.
    updateButtonInputs()
    
    // Get the current stylus input state.
    let currentInputState = getCurrentStylusInputState(relativeTo: drawingDocument.rootEntity)
    
    if let previousInputState, let currentInputState {
        // Get the drawing inputs given the current and previous input states.
        let (initialDrawingInputs, finalDrawingInputs) = getDrawingInputs(
            previousInputState: previousInputState,
            currentInputState: currentInputState,
            relativeTo: drawingDocument.rootEntity
        )
        
        // Pass the drawing inputs to the drawing document.
        drawingDocument
            .receive(
                initialDrawingInputs: initialDrawingInputs,
                finalDrawingInputs: finalDrawingInputs,
                animationDuration: appModel.animationSettings.correctionAnimationDuration,
                animateUpToTimestamp: currentInputState.finalAnchorInput.timestamp - appModel.animationSettings.correctionAnimationDelay
            )
    }
    
    // Update the previous input state and prune button inputs.
    previousInputState = currentInputState
    pruneButtonInputs()
}
```

#### Draw Strokes and Correct Them Over Time

People expect their brush strokes to appear instantly while still maintaining high visual quality. The sample addresses this challenge by implementing a dual-source drawing system that provides immediate visual feedback and refined, accurate strokes. The `DrawingDocument` class manages this dual-source approach. When the drawing document receives input, it passes the data to the drawing sources and animates between them:

```swift
class DrawingDocument {
    // ...

    /// Drawing data from the initial drawing inputs.
    private var initialDrawingSource: DrawingSource
    /// Drawing data from the final drawing inputs.
    private var finalDrawingSource: DrawingSource

    // ...

    /// Receives drawing inputs, passing them to the drawing source and
    /// animating the initial drawing source to the final drawing source.
    func receive(
        initialDrawingInputs: [DrawingInput],
        finalDrawingInputs: [DrawingInput],
        animationDuration: TimeInterval,
        animateUpToTimestamp: TimeInterval
    ) {
        // Receive initial and final drawing inputs.
        for initialDrawingInput in initialDrawingInputs {
            initialDrawingSource.receive(input: initialDrawingInput, state: brushState)
        }
        for finalDrawingInput in finalDrawingInputs {
            finalDrawingSource.receive(input: finalDrawingInput, state: brushState)
        }
        // Animate the initial drawing source to the final drawing source.
        initialDrawingSource.animate(to: finalDrawingSource, for: animateUpToTimestamp, duration: animationDuration)
    }
}
```

Here, the `animationDuration` parameter controls how long it takes for the initial stroke to correct itself into the final stroke. You can increase this parameter to make correction occur more gradually, or decrease it for faster correction.

## See Also

- [Happy Beam](happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [Setting up access to ARKit data](setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [Incorporating real-world surroundings in an immersive experience](incorporating-real-world-surroundings-in-an-immersive-experience.md)
  Create an immersive experience by making your app’s content respond to the local shape of the world.
- [Placing content on detected planes](placing-content-on-detected-planes.md)
  Detect horizontal surfaces like tables and floors, as well as vertical planes like walls and doors.
- [Tracking specific points in world space](tracking-points-in-world-space.md)
  Retrieve the position and orientation of anchors your app stores in ARKit.
- [Tracking preregistered images in 3D space](tracking-images-in-3d-space.md)
  Place content based on the current position of a known image in a person’s surroundings.
- [Exploring object tracking with ARKit](exploring_object_tracking_with_arkit.md)
  Find and track real-world objects in visionOS using reference objects trained with Create ML.
- [Object tracking with Reality Composer Pro experiences](object-tracking-with-reality-composer-pro-experiences.md)
  Use object tracking in visionOS to attach digital content to real objects to create engaging experiences.
- [Building local experiences with room tracking](building-local-experiences-with-room-tracking.md)
  Use room tracking in visionOS to provide custom interactions with physical spaces.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/drawing-in-the-air-and-on-surfaces-with-a-spatial-stylus)*