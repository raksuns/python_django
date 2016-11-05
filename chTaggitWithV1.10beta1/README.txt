# -*- coding: utf-8 -*-

1. 요점

본 예제를 실습 시 Django 1.9.X 버전에서는 정상 동작합니다.
Django 1.10b1 버전에서는,
blog 앱에서 포스트를 신규로 등록 시 다음과 같은 에러가 발생할 수 있습니다.

Cannot force an update in save() with no primary key.


2. 원인

이는 django-tagging 패키지가 Django 1.10b1 버전과 충돌하기 때문이며,
Django 역시 베타 테스트 버전이므로 어느 쪽 문제인지는 확실치가 않습니다.

만일 Django 1.10.X 공식 버전이 출시된 후에도 위와 같은 에러가 여전히 발생한다면,
3번의 해결 방법을 참고하여 조치하기 바랍니다.


3. 해결 방법

3-1. django-tagging 패키지의  2016.7월 현재 최신 버전은 0.4.3입니다.
     이보다 높은 버전으로 업그레이드 후 확인 바랍니다.

3-2. 만일 0.4.3 보다 높은 django-tagging 버전이 안 나왔다면,
     django-tagging 패키지 대신에 django-taggit 패키지를 사용하기 바랍니다.


4. chTaggitWithV1.10beta1 프로젝트는,

ch13 프로젝트를 django-taggit 패키지를 사용하여 다시 개발한 프로젝트입니다.
2016.7월 현재 Django 1.10b1 버전에서도 정상 동작하는 것을 확인하였습니다.

django-tagging 패키지를 django-taggit 패키지로 교체하면서,
변경한 파일은 다음과 같습니다.

mysite/settings.py
blog/models.py
blog/urls.py
blog/views.py
blog/templates/blog/post_detail.html
blog/templates/taggit/taggit_cloud.html


5. 본 가이드는,

2016.7월 현재 Django 1.10b1 버전은 개발 중인 베타 버전이므로,
책 본문에서는 Django 공식 버전인 1.9.7 버전을 기준으로 소스를 작성하였습니다.

2016.8월 이후 Django 1.10.X 공식 버전이 출시된 후에도,
위와 같은 에러가 발생할 수 있는 가능성이 있기 때문에 
이 상황에 대비해서 여러분이 Django 1.10.X 버전을 사용하여 실습할 수 있도록
본 가이드를 제시합니다.
