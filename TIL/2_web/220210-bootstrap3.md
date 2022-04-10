# 붓스트랩 더 연구해보기

## components

### badges

* buttons

  ```html
  <button type = "button" class = "btn btn-primary">
      Notifications <span class = "badge bg-secondary">4</span>
  </button>
  ```

* buttons - positioned

  ```html
  <button type="button" class="btn btn-primary position-relative">
    Profile
    <span class="position-absolute top-0 start-100 translate-middle p-2 bg-danger border border-light rounded-circle"> <!--profile이라는 버튼에 빨간 동그라미를 오른쪽 상단에 위치 --> 
      <span class="visually-hidden">New alerts</span> <!--이곳을 안보이게 숨기기 -->
    </span>
  </button>
  ```

* button- pill badges: 왼쪽으로 둥그렇게 만들기 - 타원형 뱃지 만들기

  ```html
  <span class = "badge rounded-pill bg-primary">Primary</span>
  ```



### buttons

* outline buttons

  ```html
  <button type="button" class="btn btn-outline-primary">Primary</button>
  <button type="button" class="btn btn-outline-secondary">Secondary</button>
  <button type="button" class="btn btn-outline-success">Success</button>
  <button type="button" class="btn btn-outline-danger">Danger</button>
  <button type="button" class="btn btn-outline-warning">Warning</button>
  <button type="button" class="btn btn-outline-info">Info</button>
  <button type="button" class="btn btn-outline-light">Light</button>
  <button type="button" class="btn btn-outline-dark">Dark</button>
  ```

* sizes

  ``` html
  <button type="button" class="btn btn-primary btn-lg">Large button</button>
  <button type="button" class="btn btn-secondary btn-lg">Large button</button>
  
  <button type="button" class="btn btn-primary btn-sm">Small button</button>
  <button type="button" class="btn btn-secondary btn-sm">Small button</button>
  ```

* disabled-button

  ```html
  <button type="button" class="btn btn-lg btn-primary" disabled>Primary button</button>
  <button type="button" class="btn btn-secondary btn-lg" disabled>Button</button>
  
  혹은
  <a class="btn btn-primary btn-lg disabled" role="button" aria-disabled="true">Primary link</a>
  <a class="btn btn-secondary btn-lg disabled" role="button" aria-disabled="true">Link</a>
  ```

* block buttons: 엄청 긴 한 페이지를 다 가로막고 있는 버튼

  ```html
  <div class="d-grid gap-2">
    <button class="btn btn-primary" type="button">Button</button>
    <button class="btn btn-primary" type="button">Button</button>
  </div>
  
  중간에만 위치한 블록- 위치를 지정 가능
  <div class="d-grid gap-2 col-6 mx-auto">
    <button class="btn btn-primary" type="button">Button</button>
    <button class="btn btn-primary" type="button">Button</button>
  </div>
  
  위치 지정하면서 크기도 직접 지정 가능
  <div class="d-grid gap-2 d-md-flex justify-content-md-end">
    <button class="btn btn-primary me-md-2" type="button">Button</button>
    <button class="btn btn-primary" type="button">Button</button>
  </div>
  ```

  

  