const handleLike = (postId) => {
  const likesText = document.querySelector(`#likes-text-${postId}`)
  const likesLabel = document.querySelector(`#likes-label-${postId}`)

  if (!likesLabel.classList.contains('red')) {
    fetch(`/posts/${postId}/likes`, { method: 'PUT' }).then((response) => {
      if (response.ok) {
        likesText.innerHTML = Number(likesText.innerHTML) + 1
        likesLabel.classList.add('red')
      }
    })
  } else {
    fetch(`/posts/${postId}/likes`, { method: 'DELETE' }).then((response) => {
      if (response.ok) {
        likesText.innerHTML = Number(likesText.innerHTML) - 1
        likesLabel.classList.remove('red')
      }
    })
  }
}
