import pytest
from django.urls import reverse
from .models import Post


@pytest.mark.django_db
def test_post_str():
    post = Post.objects.create(
        title='Test title',
        slug='test-title',
        content='Test content',
    )
    assert str(post) == 'Test title'

@pytest.mark.django_db
def test_post_list_view(client):
    post = Post.objects.create(
        title='Another test',
        slug='another-test',
        content='Some content here',
    )
    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200
    assert post.title in response.content.decode()

@pytest.mark.django_db
def test_post_detail_view(client):
    post = Post.objects.create(
        title='Detail test',
        slug='detail-test',
        content='Detail content',
    )
    url = reverse('post_detail', args=[post.slug])
    response = client.get(url)
    assert response.status_code == 200
    assert 'Detail content' in response.content.decode()
