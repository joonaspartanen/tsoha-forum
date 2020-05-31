const logout = () => {
  document.getElementById('logout-form').submit()
}

const handleLike = (postId) => {
  const likesText = document.querySelector(`#likes-text-${postId}`)
  const likesLabel = document.querySelector(`#likes-label-${postId}`)

  if (!likesLabel.classList.contains('red')) {
    fetch(`/posts/${postId}/likes`, {
      method: 'PUT',
      headers: {
        Accept: 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          likesText.innerHTML = Number(likesText.innerHTML) + 1
          likesLabel.classList.add('red')
        }
      })
  } else {
    fetch(`/posts/${postId}/likes`, {
      method: 'DELETE',
      headers: { Accept: 'application/json' },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          likesText.innerHTML = Number(likesText.innerHTML) - 1
          likesLabel.classList.remove('red')
        }
      })
  }
}

const handleDeleteTopic = (topicId) => {
  fetch(`/topics/${topicId}`, { method: 'DELETE' }).then((response) => {
    if (response.ok) {
      const topicWrapper = document.querySelector(`#topic-wrapper-${topicId}`)
      topicWrapper.parentNode.removeChild(topicWrapper)
    }
  })
}

const handleEditTopic = (topicId) => {
  const topicWrapper = document.querySelector(`#topic-wrapper-${topicId}`)
  const topicSubject = topicWrapper.getElementsByTagName('h3')[0]
  const topicSubjectText = topicSubject.getElementsByTagName('a')[0]
  const input = document.createElement('input')
  input.classList.add('topic-subject-input')
  input.minLength = 1
  input.maxLength = 100
  topicSubject.replaceWith(input)
  input.select()
  input.value = topicSubjectText.innerHTML
  input.addEventListener('keyup', (event) => {
    if (event.keyCode === 13) {
      event.preventDefault()
      const newSubject = input.value
      const data = { Subject: newSubject }
      fetch(`/topics/${topicId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      }).then((response) => {
        if (response.ok) {
          topicSubjectText.innerHTML = newSubject
          input.replaceWith(topicSubject)
        }
      })
    }
  })
}
