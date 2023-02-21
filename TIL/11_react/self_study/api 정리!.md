# api 정리!

src/api 안에 모든 api 정리!

src/api/해당하는 api.jsx

```jsx
import https from "./https.jsx";

export async function api함수이름(CartVO) {
  // 이건 나중에 login, signup 완전히 구현되면 사용
  // 꼭 사용자인거 인증해야할 때!
  // const accessToken = sessionStorage.getItem("access-token");
  // https.defaults.headers.common["access_token"] = accessToken;

  return new Promise((resolve) => {
    https
      .post혹은get("api 주소", post일 경우 parameter)
      .then((response) => {
        if (response.status === 200) {
          resolve(response.data);
        } else {
          resolve(response);
        }
      })
      .catch((e) => {
        console.log(e);
      });
  });
}

```



해당 jsx 파일에 쓸 내용

```jsx
import {api함수이름} from api함수가 있는 디렉토리
const 함수이름 = async () => {
    const res = await api함수이름(post일 경우 parameter);
    console.log(res.data);
    
    // 이때부터는 마음대로 함수 사용
}
```



## example

```jsx
// src/api/cart.jsx

import https from "./https.jsx";

export async function insertCart(CartVO) {
  // const accessToken = sessionStorage.getItem("access-token");
  // https.defaults.headers.common["access_token"] = accessToken;

  return new Promise((resolve) => {
    https
      .post("/cart/insert", CartVO)
      .then((response) => {
        if (response.status === 200) {
          resolve(response.data);
        } else {
          resolve(response);
        }
      })
      .catch((e) => {
        console.log(e);
      });
  });
}

```

```jsx
import { insertCart } from "../../api/cart";
const cartInsert = async () => {
    const res = await insertCart(CartVO);
    alert("장바구니에 담겼습니다.");
    console.log(res.data);
};
```

