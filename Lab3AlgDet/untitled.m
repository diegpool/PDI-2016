%for i=1:1
% red(1,1,1)= 70/255; red(1,1,2) = 32/255; red(1,1,3) = 32/255;
% %green(1,1,1)= 101/255; green(1,1,2) = 97/255; green(1,1,3) = 97/255; 
% 
% d1 = 480;
% d2 = 640;
% 
% A = zeros(1,1,3);
% B = A;
% numpixA = 0;
% numpixB = 0;
% tolRho = 0.15;
% 
% for i=1:d1
%     for j = 1:d2
%         temp = img(i,j,:);
%         if( norm3D(temp - red) <= tolRho )
%             A = A + temp;
%             numpixA = numpixA + 1;
%         else
%             B = B+temp;
%             numpixB = numpixB +1;
%         end
%     end
% end
% 
% A = A/numpixA;
% B = B/numpixB;
% rho = calRho(A,B);
%end