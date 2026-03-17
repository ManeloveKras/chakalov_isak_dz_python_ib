# АНАЛИЗ + ГРАФИКИ (Этапы 2-3 ✅)
print("🔍 Анализ по типам событий (signature):")
signature_counts = df['signature'].value_counts()
top_10 = signature_counts.head(10)
print(top_10)

# НАСТРОЙКА ГРАФИКОВ
plt.style.use('default')
sns.set_palette("husl")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# SEABORN BARPLOT
sns.barplot(x=top_10.values, y=top_10.index, ax=ax1, palette="viridis")
for i, v in enumerate(top_10.values):
    ax1.text(v + 2, i, str(v), va='center', fontweight='bold', fontsize=11)
ax1.set_title('Распределение событий ИБ\n(Seaborn Barplot)', fontsize=14, pad=20)
ax1.set_xlabel('Количество событий')

# MATPLOTLIB PIE
colors = plt.cm.Set3(range(len(top_10)))
ax2.pie(top_10.values, labels=top_10.index, autopct='%1.1f%%', 
        startangle=90, colors=colors)
ax2.set_title('Доля типов событий\n(Matplotlib Pie)', fontsize=14, pad=20)

plt.tight_layout()
plt.savefig('RESULT.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("✅ ГРАФИКИ СОЗДАНЫ!")
print("📁 Файлы: events.json + RESULT.png")
