"""5. Nested Data Independence (Deep Copy)
A school stores classroom data:
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
Scenario:
● Create a deep copy of this structure.
● Modify student count in original.
Task:
● Prove that copied data remains unchanged.
● Explain why deep copy is required here."""


import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

# Create deep copy
new_classes = copy.deepcopy(classes)

# Modify original data
classes[0][1][0] = 50

print("Original data:", classes)
print("Copied data:", new_classes)
