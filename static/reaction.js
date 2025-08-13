async function updateReactionCount() {
  const res = await fetch('/reaction-count');
  const data = await res.json();
  document.getElementById('reaction-count').textContent = data.count + ' reactions';
}

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('like-btn').addEventListener('click', async () => {
    await fetch('/react', { method: 'POST' });
    updateReactionCount();
  });

  updateReactionCount();
});
