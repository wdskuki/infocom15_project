N = 100;
b1 = [0.3, 1, 10, 30, 50, 70, 90];
b2 = 120;
ni = 14;
ki = 8;
di = 10;
loopNum = 100;

rd_bwMeans = [];
rd_bwStd = [];
rd_timeMeans = [];
rd_timeStd = [];

fpsn_bwMeans = [];
fpsn_bwStd = [];
fpsn_timeMeans = [];
fpsn_timeStd = [];

spsn_bwMeans = [];
spsn_bwStd = [];
spsn_timeMeans = [];
spsn_timeStd = [];
    
for i = 1 : length(b1)
   filename_bw =  sprintf('../output/bw_%s_%s_%s_%s_%s_%s_%s.txt', ...
       num2str(N), num2str(b1(i)), num2str(b2), num2str(ni), num2str(ki), num2str(di),num2str(loopNum));
   filename_time =  sprintf('../output/time_%s_%s_%s_%s_%s_%s_%s.txt',...
       num2str(N), num2str(b1(i)), num2str(b2), num2str(ni), num2str(ki), num2str(di),num2str(loopNum));
   output_bw= load(filename_bw);
   output_time = load(filename_time);
   
   mean_bw = mean(output_bw);
   mean_time = mean(output_time);
   std_bw = std(output_bw);
   std_time = std(output_time);
   
    rd_bwMeans(i) = mean_bw(1);
    rd_bwStd(i) = std_bw(1);
    rd_timeMeans(i) = mean_time(1);
    rd_timeStd(i) = std_time(1);

    fpsn_bwMeans(i) = mean_bw(2);
    fpsn_bwStd(i) = std_bw(2);
    fpsn_timeMeans(i) = mean_time(2);
    fpsn_timeStd(i) = std_time(2);

    spsn_bwMeans(i) = mean_bw(3);
    spsn_bwStd(i) = std_bw(3);
    spsn_timeMeans(i) = mean_time(3);
    spsn_timeStd(i) = std_time(3);
end

Y_bwMeans = [rd_bwMeans', fpsn_bwMeans', spsn_bwMeans'];
Y_bwStd = [rd_bwStd', fpsn_bwStd', spsn_bwStd'];

Y_timeMeans = [rd_timeMeans', fpsn_timeMeans', spsn_timeMeans'];
Y_timeStd = [rd_timeStd', fpsn_timeStd', spsn_timeStd'];

titleStr='';
figure(1);

pBW = bar(Y_bwMeans);
hold on;
errorbar(Y_bwMeans, Y_bwStd, '+');

%p = plot(b1, rd_bwMeans,'-rv', b1, fpsn_bwMeans, '-k<',  b1, spsn_bwMeans, '-go');

ylabel('BottleNetBW(MB/s)');
xlabel('link BW range(MB/s)');
title( sprintf('rd vs fpsn vs spsn \n (N = %s, ni = %s, ki = %s, di = %s, loopNum = %s)',...
    num2str(N), num2str(ni), num2str(ki), num2str(di), num2str(loopNum)));
legend('rd', 'fpsn', 'spsn');
set(pBW,'LineWidth',1.0);
    
    