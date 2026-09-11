# Creating animation graphs with Reality Composer Pro and RealityKit

**Framework**: visionOS

Animate RealityKit entities using blend spaces and state machines with the Animation Graph feature.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- Xcode 27.0+

#### Overview

This sample code project demonstrates how to create an [`AnimationGraphComponent`](https://developer.apple.com/documentation/realitykit/animationgraphcomponent) inside Reality Composer Pro 3 to procedurally drive an owl’s animations using Swift. An animation graph is a data driven way to describe how an entity’s animations change over time. Animation graphs use simple parameters and conditions to sequence and blend animations in ways that can be complicated to manage by hand in code. This sample uses an `AnimationGraphComponent` to drive an owl’s pose based on parameters like the owl’s speed.

> **Note**: For more details on navigating the Reality Composer Pro’s user interface, visit [`Working with the Animation Graph`](https://developer.apple.com/documentation/realitycomposerpro/working-with-the-animation-graph).

#### Prepare Your Animations

The sample authors its animation graph inside of [`Reality Composer Pro`](https://developer.apple.com/documentation/realitycomposerpro). Before preparing the animation graph, you import the model and animations you plan to use by either dragging and dropping the USD files into the Project Browser or by clicking the import button on the top left of the Project Browser tab and selecting your assets.

![A screenshot of the Project Browser tab within Reality Composer Pro. The import button is highlighted and a list of imported animations are shown.](/images/com.apple.visionOS/AnimationGraphs-ImportAssets@2x.png)

The animations in this sample loop seamlessly. Adjust the repeat behavior of animations by selecting the imported asset in the project browser, then expand the Animation Settings drop-down menu, and change Repeat Mode to Repeat.

![A screenshot of the Animation Settings of an asset within Reality Composer Pro. A drop-down menu is visible for Repeat Mode to select the Repeat value.](/images/com.apple.visionOS/AnimationGraphs-AnimationSettings@2x.png)

#### Create an Animation Graph

The sample creates an animation graph asset in the root of the Reality Composer Pro project named Owl Animation Graph. The animation graph uses the `owl_skeldef` and Owl Character imported assets for its Skeleton Definition and Preview Entity, respectively.

![A screenshot of the Inspector panel of Reality Composer Pro. The Owl Animation Graph asset is selected. The Skeleton Definition drop-down menu is open, and owl_skeldef is hovered for the selected entry.](/images/com.apple.visionOS/AnimationGraphs-GraphSettings@2x.png)

The sample creates two input parameters for the Owl Animation Graph. First, `moving` is a Boolean parameter that changes the graph between a perched and flying state. Then, `speed` is a float parameter that controls a blend between an in-place hovering animation and a faster-moving flying animation.

![A screenshot of the inputs for an animation graph. There are two inputs in a table for moving and speed.](/images/com.apple.visionOS/AnimationGraphs-Inputs@2x.png)

The Owl Animation Graph contains a Blend 1D node to drive the owl’s pose while it’s moving. The `speed` parameter of the graph controls the blending of two incoming animations. Two Animation Clip nodes, one for hover and one for fly, link into the blend node.

Hover connects into the first input at position `0` within the blend space, and fly connects into the second input at position `1`. The blend space node connects into a state machine node’s Moving input parameter. This parameter represents the animation that plays during the Moving state of that state machine.

Another Animation Clip node for the perch animation connects into a Perched state on the state machine. The final output pin of the state machine connects to the Final Pose node of the animation graph and selects the blend space and perch animations based on the provided state machine.

![A screenshot of Reality Composer Pro's animation graph editor. On the left, a graph canvas shows six connected nodes: two Animation Clip nodes labeled Hover and Fly that are wired into a central Blend 1D node that has an output port which connects to the Moving input of a State Machine node. Another Animation Clip node labeled Perch connects to the Perched input of the state machine node. The output of the state machine node connects to a Final Pose node. On the right, the inspector panel for the Blend 1D node shows a horizontal blend space with a slider from 0 to 1 with handles at each end. The left handle is blue. Below that, the Name (hover) and Position (0) properties of the selected handle are shown. A line separates that section and a value called parameter which is set to speed.](/images/com.apple.visionOS/AnimationGraphs-GraphSetup@2x.png)

The Owl Animation Graph uses a state machine with two states, Moving and Perched, to determine its final pose. This sample configures the perch state to be the start state, and places a transition from perched to moving, which responds to a true `moving` state. Another transition from moving to perched uses the opposite condition.

![A screenshot of Reality Composer Pro's animation graph editor. On the left, a graph canvas shows two state nodes Moving and Perched. Two arrows with a green dot connects both states, one arrow points toward each of the states. The right arrow is highlighted blue and points towards Perched. On the right, the inspector panel for a transition shows properties for Reset Target (false), Blend Duration (0.2) and Blend Curve (a graph of an ease-in-out curve). Below that is a list of conditions with a single entry. The entry has a green dot at the front, then shows the moving parameter, an equality sign, and then finally the value false.](/images/com.apple.visionOS/AnimationGraphs-StateMachine@2x.png)

The two parameters `speed` and `moving` procedurally control which animation is playing for the owl.

> 💡 **Tip**: To test out the graph, press play at the top of a Reality Composer Pro window, then modify the parameters and review the behavior in real time.

#### Prepare an Entity Hierarchy

This sample loads the `world` entity asset from the Reality Composer Pro project. Select the `owl_model`, add an [`AnimationGraphComponent`](https://developer.apple.com/documentation/realitykit/animationgraphcomponent), and assign the Owl Animation Graph component to it.

> **Note**: You can only place `AnimationGraphComponent` on entities with a `Skeleton` component.

To test changes within your app, export the `world` entity asset from Reality Composer Pro. Either export the entity directly using the context menu on the `world` asset, or by launching the app using the Run with Xcode workflow. For more information on Xcode linking and the Run with Xcode workflow, see  [`Configuring the project workspace`](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-configuringprojectworkspace).

#### Drive the Animation Graph From Your Application

The [`AnimationGraphComponent`](https://developer.apple.com/documentation/realitykit/animationgraphcomponent) reads the [`parameters`](https://developer.apple.com/documentation/realitykit/entity/parameters) to drive its state during runtime. The sample keeps track of the values for `moving` and `speed` on the `ContentView`, as seen below. The sample displays controls for these values on the window toolbar of the application.

```swift
struct ContentView: View {
    @State var owl: Entity?
    @State var moving = false
    @State var speed: Float = 0.0

    // ...

    @ViewBuilder
    var animationControls: some View {
        Toggle("Moving", isOn: $moving)
        Slider(value: $speed, in: 0...1) {
            Text("Speed")
        }
    }
}
```

When the sample constructs its [`RealityView`](https://developer.apple.com/documentation/realitykit/realityview), it loads the `world` [`Entity`](https://developer.apple.com/documentation/realitykit/entity) exported from Reality Composer Pro. Then, it assigns default values to the owl `Entity` within that hierarchy, like this:

```swift
// Load the world scene from the reality file
// Reality Composer Pro exported.
let mainScene = try await Entity(named: OwlConstants.worldEntity)
content.add(mainScene)

// Find the owl entity in the scene.
self.owl = mainScene.findEntity(named: OwlConstants.owlName)
guard let owl else {
    // ...
}

// Assign initial values to animation parameters.
owl.parameters[OwlConstants.movingParameter] = BindableValue(moving)
owl.parameters[OwlConstants.speedParameter] = BindableValue(speed)
```

When users modify the properties in the UI, the sample uses [`onChange(of:perform:)`](https://developer.apple.com/documentation/swiftui/view/onchange(of:perform:)) callbacks to detect the changes and propagate them to the entity like so:

```swift
var body: some View {
    VStack {
        RealityView { content in
            // ...
        }.onChange(of: moving) {
            owl?.parameters["moving"]?.value = moving
        }.onChange(of: speed) {
            owl?.parameters["speed"]?.value = speed
        }
        // ...
    }
}
```

The `AnimationGraphComponent` reads from the entity’s `parameters` to drive the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/creating-animation-graphs-with-reality-composer-pro-and-realitykit)*