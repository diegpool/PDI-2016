clear all ; close all; clc;
img = double(imread('prueba5.jpg'))./255;

red(1,1,1)= 237/255; red(1,1,2) = 28/255; red(1,1,3) = 36/255;
green(1,1,1)= 34/255; green(1,1,2) = 177/255; green(1,1,3) = 76/255; 

d = 600;

A = zeros(1,1,3);
B = A;
numpixA = 0;
numpixB = 0;
tolRho = 0.7;
maximo1 = inf ;
maximo2 = maximo1;
for i=1:d
    for j = 1:d
        temp = img(i,j,:);
        if( norm3D(temp - red) <= tolRho )
            A = A + temp;
            if(norm3D(temp-red)<maximo1)
                maximo1=norm3D(temp-red);
            end
            numpixA = numpixA + 1;
        elseif( norm3D(temp - green) <= tolRho )
            B = B+temp;
            
            if(norm3D(temp-green)<maximo2)
                maximo2=norm3D(temp-green);
            end
            numpixB = numpixB +1;
        end
    end
end

A = A/numpixA;
B = B/numpixB;
rho = calRho(A,B);
%%
imges=[img(:,1,:) img img(:,end,:)];
imges=[imges(1,:,:); imges ;imges(end,:,:)];
imgBorde=zeros(d,d,3);
tolBorde = 1;

for i=1:d-1;
    for j=1:d;
    
        Atemp = imges(i+1,j,:);
        Btemp = imges(i+1,j+2,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
        
        Atemp = imges(i,j+1,:);
        Btemp = imges(i+2,j+1,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
    end
    
end

figure;
imshow(img);
figure;
imshow(imgBorde);
