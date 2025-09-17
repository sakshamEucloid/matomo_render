# from growthbook import GrowthBook

# def on_experiment_viewed(experiment, result):
#   # TODO: Use your real analytics tracking system
#   print("Viewed Experiment")
#   print("Experiment Id: " + experiment.key)
#   print("Variation Id: " + result.key)

# gb = GrowthBook(
#   api_host = "http://localhost:3100",
#   client_key = "sdk-EMr67bTFgH00gWb",
#   on_experiment_viewed = on_experiment_viewed
# )

# gb.load_features()

# if gb.is_on("bigger-see-more"):
#   print("Feature is enabled!")


from growthbook import GrowthBook

# User attributes for targeting and experimentation
attributes = {
  "id": "1234",
  "customUserAttribute": "foot"
}

def on_experiment_viewed(experiment, result):
  # Use whatever event tracking system you want
  analytics.track(attributes["id"], "Experiment Viewed", {
    'experimentId': experiment.key,
    'variationId': result.variationId
  })

# Create a GrowthBook instance
gb = GrowthBook(
  api_host = "http://localhost:3100",
  client_key = "sdk-EMr67bTFgH00gWb",
  on_experiment_viewed = on_experiment_viewed,
  attributes=attributes
)

# Load features from the GrowthBook API with caching
gb.load_features()
print(gb)

# Simple on/off feature gating
if gb.is_on("bigger-see-more"):
  print("My feature is on!")

# Get the value of a feature with a fallback
color = gb.get_feature_value("button-color-feature", "blue")