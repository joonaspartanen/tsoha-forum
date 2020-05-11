const handleLike = (postId) => {
  const likeLabel = document.querySelector(`#likes-label-${postId}`)
  fetch(`posts/${postId}`, { method: 'POST' }).then((response) => {
    likeLabel.innerHTML = Number(likeLabel.innerHTML) + 1
  })
}
