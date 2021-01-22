# Write your MySQL query statement below
​
SELECT DISTINCT ad_id, IFNULL(ROUND((nclick/ (nclick+nviews)*100),2),0) as ctr
FROM
    (SELECT DISTINCT ad_id, action,
        (SELECT COUNT(*) FROM Ads b WHERE action='Clicked' AND a.ad_id= b.ad_id ) as nclick, 
        (SELECT COUNT(*) FROM Ads b WHERE action='Viewed' AND a.ad_id= b.ad_id ) as nviews
    FROM Ads a
    ) AS totals
ORDER BY ctr DESC, ad_id ASC 
 
​
