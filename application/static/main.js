const logout = () => {
  document.getElementById('logout-form').submit()
}

const handleLike = (postId, topicId) => {
  const likesText = document.querySelector(`#likes-text-${postId}`)
  const likesLabel = document.querySelector(`#likes-label-${postId}`)

  if (!likesLabel.classList.contains('red')) {
    fetch(`/topics/${topicId}/posts/${postId}/likes`, {
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
    fetch(`/topics/${topicId}/posts/${postId}/likes`, {
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

const giveAdminRights = (userId) => {
  fetch(`/auth/users/${userId}/admin`, {
    method: 'POST',
  }).then((response) => {
    if (response.ok) {
      const button = document.querySelector(`#give-admin-rights-button-${userId}`)
      const adminRightsCell = document.querySelector(`#admin-rights-cell-${userId}`)
      button.innerHTML = 'Admin rights granted'
      button.classList.add('disabled')
      adminRightsCell.innerHTML = 'Yes'
    }
  })
}

const removeAdminRights = (userId) => {
  fetch(`/auth/users/${userId}/admin`, {
    method: 'DELETE',
  }).then((response) => {
    if (response.ok) {
      const button = document.querySelector(`#remove-admin-rights-button-${userId}`)
      const adminRightsCell = document.querySelector(`#admin-rights-cell-${userId}`)
      button.innerHTML = 'Admin rights removed'
      button.classList.add('disabled')
      adminRightsCell.innerHTML = 'No'
    }
  })
}

const handlePostDelete = (postId, topicId) => {
  fetch(`/topics/${topicId}/posts/${postId}`, {
    method: 'DELETE',
  }).then((response) => {
    if (response.ok) {
      const post = document.querySelector(`#post-${postId}`)
      post.parentNode.removeChild(post)
    }
  })
}
