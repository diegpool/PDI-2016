clear all ; close all; clc;
img = double(imread('prueba.png'))./255;

red = img(1,end,:);
green = img(1,1,:);

d = 600;

% img = zeros(d,d,3);
% 
% for i=1:d
%     for j = 1:d
%         if(j<d/2)
%             img(i,j,:) = red;
%         else 
%             img(i,j,:) = green;
%         end
%     end
% end
A = zeros(1,1,3);
B = A;
numpixA = 0;
numpixB = 0;

for i=1:d
    for j = 1:d
        temp = img(i,j,:);
        if( norm3D(temp - red) <= 1e-3 )
            A = A + temp;
            numpixA = numpixA + 1;
        elseif( norm3D(temp - green) <= 1e-3 )
            B = B+temp;
            numpixB = numpixB +1;
        end
    end
end

A = A/numpixA;
B = B/numpixB;
rho = calRho(A,B);
imges=[img(:,1,:) img img(:,end,:)];
imges=[imges(1,:,:); imges ;imges(end,:,:)];
imgBorde=zeros(d,d,3);
imgVert = imgBorde;
imgHor = imgBorde;

%Detector Vertical
for i=1:d-1;
    for j=1:d;
    
        Atemp = imges(i+1,j,:);
        Btemp = imges(i+1,j+2,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<1e-3); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<1e-3;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
    end    
end

%Detector horizontal
for i=1:d-1;
    for j=1:d;
        Atemp = imges(i,j+1,:);
        Btemp = imges(i+2,j+1,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<1e-3); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<1e-3;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
    end
end

figure;
imshow(img);
figure;
imshow(imgBorde);
