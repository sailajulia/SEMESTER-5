import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Draw the central circle
central_circle = plt.Circle((0, 0), 0.3, color="black", fill=True)
ax.add_patch(central_circle)

# Draw four lines extending outward
line_width = 0.3
for i in range(4):
    angle = i * 90
    if angle == 0:
        ax.plot([0, 0], [0.3, 2.5], color="black", linewidth=line_width * 10)
    elif angle == 90:
        ax.plot([0.3, 2.5], [0, 0], color="black", linewidth=line_width * 10)
    elif angle == 180:
        ax.plot([0, 0], [-0.3, -2.5], color="black", linewidth=line_width * 10)
    elif angle == 270:
        ax.plot([-0.3, -2.5], [0, 0], color="black", linewidth=line_width * 10)

# Add "+" symbols
ax.text(-2.7, 2.5, "+", fontsize=25, color="black", weight='bold')
ax.text(2.5, -2.5, "+", fontsize=25, color="black", weight='bold')

# Add text for "INFIL PRODUCT"
ax.text(0, -3, "INFIL", ha='center', va='center', fontsize=30, fontweight='bold')
ax.text(0, -3.5, "PRODUCT", ha='center', va='center', fontsize=12, color='grey')

# Remove axes
ax.axis("off")

plt.show()
