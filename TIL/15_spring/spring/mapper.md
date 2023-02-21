# mapper.xml

java 프로젝트에는 

* project > src > main > java.com.project_name.cart 
  * Contoller.java, Mapper.java, Service.java, VO.java, ServiceImpl.java가 있음
* project > src > main > resources.com.project_name.cart
  * Mapper.xml에는 sql 문이 작성이 되어있어서 mapper.xml을 공부해보자!



## cart

장바구니 담을 때 사용했던 mapper



### cartFind

해당 멤버의 카트에 대한 정보 가져오기

장바구니에 대한 상품의 정보를 가져오기 위해서는 product 테이블 조인이 필요

```sql
select * 
from cart c 
join product p
on c.product_product_no = p.product_no
where c.member_member_no = #{member_no}
```



#{}와 ${}의 차이

* #{}
  * string 형태로 값을 넣어주고 따옴표가 자동 삽입
  * 보안에 좋음
* ${}
  * 값이 바로 삽입
  * 컬럼명 혹은 예약어를 바로 주입할 때 보통 사용 가능
  * 보안에 취약



### cartReset

해당 멤버의 카트 전체 초기화

```sql
delete from cart where member_member_no = #{member_no}
```



### cartInsert

상품을 장바구니에 담기

```sql
insert into cart (cart_count_amount, member_member_no, product_product_no, store_store_no)
values (#{cart_count_amount}, #{member_member_no}, #{product_product_no}, #{store_store_no})
```



### cartDelete

카트번호에 해당하는 장바구니 삭제

```xml
<delete parameterType="java.util.List">
	delete from cart
	<where>
		<foreach item="vol" collection="list" separator="or">
			(cart_no = #{vol.cart_no} and member_member_no = #{vol.member_member_no})
    	</foreach>
	</where>
</delete>
```



* foreach 문 지원 태그
  * collection: 전달받은 인자, list or array 형태만 가능
  * item: 전달받은 인자 값을 alias 명으로 대체
  * open: 구문이 시작될 때 삽입할 문자열
  * close: 구문이 종료될 때 삽입할 문자열
  * seperator: for문 반복 되는 사이에 출력할 문자열
  * index: 반복되는 구문 번호이다. 0부터 순차적으로 증가



### cartList

product 뿐만 아니라 store에 대한 정보도 가져오기 위한 장바구니 정보 조회

```sql
select * from cart
join product p
on cart.product_product_no = product.product_no
join store s
on p.store_store_no = s.store_no
where cart.cart_ no in (select cart_cart_no from orders where member_member_no = #{member_member_no})
```



## member

회원관리를 위해 사용했던 mapper



### memberFind

아이디와 비밀번호를 가지고 로그인

```xml
<select>
	select * from member where id = #{id} and password = #{password}
</select>
```



### memberJoin

아이디, 비밀번호, 포인트(초기값: 0), 전화번호, 이메일, 동의 여부, 이름, 스탬프 개수(초기값:0)으로 회원가입

```xml
<Insert>
	Insert into member (id, password, point, phone_number, email, agree, mname, stamp )
    values (#{id}, #{password}, 0, #{phone_number}, #{email}, #{agree}, #{mname}, 0)
</Insert>
```



### memberFindId

전화번호 이름을 사용하여 아이디 찾기

```xml
<select>
	select * from member where phone_number = #{phone_number}
</select>
```



### memberFindPwd

아이디와 전화번호를 가지고 비밀번호 찾기

```xml
<select>
	select * from member where id=#{id} and phone_number = #{phone_number}
</select>
```



### memberCheckId

아이디가 중복되어있는지 체크

```sql
select * from member where id = #{id}
```

만약 해당 아이디에 대한 정보가 이미 존재한다면 0을 return 함

없다면 넘어감



### memberStamp

주문을 한다면 멤버의 스탬프 개수를 증가

```xml
<update>
	update member set stamp = stamp + #{stamp}, point = point + #{point} where member_no = #{member_no} 
</update>
```



### memberInfo

멤버 정보 조회

```sql
select * from member where member_no = #{member_no}
```



### changeInfo

회원 정보 수정

```xml
<update>
	update member set email=#{email}, phone_number=#{phone_number}, password=#{password} where member_no=#{member_no}
</update>
```



## orders

구매내역을 조회하기 위해 사용했던 mapper



### ordersInsert

구매내역에 추가

```sql
insert into orders (product_product_no, member_member_no, count_amount, store_store_no)
values (#{product_product_no}, #{member_member_no}, #{count_amount}, #{store_store_no})
```



### cartToOrders

장바구니에서 결제 내역으로 넘어갈 때 사용

```xml
<insert>
	INSERT INTO orders (member_member_no, cart_cart_no, count_amout, product_product_no) 
    values
    <foreach separator="," collection="list" item="vol">
    	(#{vol.member_member_no}, #{vol.cart_cart_no}, #{vol.count_amount}, #{vol.product_product_no})
    </foreach>
</insert>
```

많은 데이터를 한번에 테이블에 insert 할 수 있기 때문에 separator를 ','을 써서 다수 데이터 삽입



### recentPaymentDetail

최근 결제 내역 날짜 descending 으로 가져오기

```sql
select * from payment_detail pd
join payment p
on pd.payment_payment_no = p.payment_no
join product pro
on pd.product_product_no = pro.product_no
join store s
on pro.store_store_no = s.store_no
where payment_payment_no = 
	(select payment_no 
     from payment 
     where member_no = #{member_member_no}
    order by payment_no desc
    limit 1)
    
```



## payment

결제하기 위해 사용했던 mapper

장바구니에서 결제하기로 넘기거나, 상품 조회에서 결제하기 버튼을 눌렀을 때 사용



### paymentDetailFind

결제창으로 넘어간 정보들 조회, 상품, 매장에 대한 모든 정보를 가져와야함

```sql
select *
from payment pay
join payment_detail pd
on pay.payment_no = pd.payment_payment_no
join product p
on pd.product_product_no = p.product_no
join store s
on pay.store_store_no = p.product_no
where payment_member_member_no = #{member_no}
order by payment_no desc
```



### paymentDetailInsert

결제창에 보낼 수량, 결제 번호, 회원번호, 상품 번호, 매장 번호 삽입

```xml
<insert>
	insert into payment_detail (amount, payment_payment_no, payment_member_member_no, product_product_no, product_store_store_no ) 
    values
    <foreach item="vol" collection="list" separator=",">
    	(#{vol.amount}, #{vol.payment_payment_no}, #{vol.payment_member_member_no}, #{vol.product_product_no}, #{vol.product_store_store_no})
    </foreach>
</insert>
```





## paymentdetail

결제에 대한 세부 정보를 조회하기 위한 mapper



### paymentDetailFind

```sql
select * 
from payment_detail pd join product p
on pd.product_product_no = p.product_no
where payment_payment_no = #{payment_no}
```



## product



### productListFind

첫 화면 페이지에 주변의 매장 정보를 목차로 보여줌 이때, 너무 많으면 안돼서 10개만 보여줌

```sql
select * from product where store_store_no=#{store_no} limit 10
```



### productSearchListFind

브랜드가 이마트, 스타벅스로 나뉘기 때문에  해당하는 branch_name 중에  value 이름이 포함된 매장을 찾아야함

```sql
select * from product p
join store s
on p.store_store_no = s.store_no
where pname like '%${search_value}%' and branch_name=#{branch_name}
```



* like : 조건절 where 안에 들어갈 수 있으며 글자수를 지정해주지 않음
  * 글자수를 지정해주는건 _
  * where  변수 like '%blahblah%'



## productItem



### productFindItem

찾는 상품 번호에 해당하는 상품을 찾기

```sql
select * from product where product_no = ${searchProductNo}
```



## store

매장 정보를 조회하기 위한 mappper



### storeFind

내 현재 위치 위도 경도를 이용해 내 주변 1km 반경 안에 매장 리스트 조회

```xml
<select>
    <![CDATA[
	SELECT *,
		   (6371*acos(cos(radians(#{latitude}))*cos(radians(latitude))*cos(radians(#{longtitude}) - radians(longtitude)) + sin(radians(#{latitude})) * sin(radians(latitude)))) as distance,
		   if((select count(*) from store_like where store_store_no = store.store_no and member_member_no=#{member_no}) > 0, '1', '0') as store_likes
	FROM store 
	WHERE (6371*acos(cos(radians(#{latitude}))*cos(radians(latitude)) * cos(radians(#{longtitude})-radians(longtitude)) + sin(radians(#{latitude})) * sin(radians(latitude)))) < 0.3 and branch_name = #{branch_name}
	ORDER BY distance
	]]>
</select>
```



* CDATA

  * (Unparsed) Character Data

  * 파싱하지 않는 문자 데이터 

  * 안에 들어가는 텍스트가 파싱되지 않게 하는 기능을 함
  * 위의 코드 같은 경우 이하, 이상을 보여주는 `>` 특수문자가 있기 때문에 cdata로 지정해야 파싱처리 되지 않고 진행 가능

  * 반대로, 파싱하는 문자 데이터는 PCDATA



* if 절
  *  if (조건문, 참일 때 값, 거짓일 때 값)
  * if((select count(*) from table where --- ) > 0, '1', '0')
    * select --- 값이 0보다 크면 1, 아니면 0 



### myStoreDelete

내가 자주 찾는 장소로 지정한 매장 삭제하기 - 자주 찾는 매장에서 삭제

```sql
delete from store_like
where member_member_no = #{member_no} and store_store_no = #{store_no}
```



### storeSearch

입력된 input값과 해당 브랜치 이름(스타벅스 or 이마트24)으로 매장 검색하기

```sql
select * from store where brand_name like '%${search_word}%' and branch_name = #{branch_name}
```

